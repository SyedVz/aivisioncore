import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import cv2 as cv
import math
from .models.cnn_detector import CNNDetector
from .models.clip_detector import CLIPDetector
from .models.yolo_detector import YoloDetector
from .thingspace.gateway_client import GatewayClient
from .imp_platform.imp_client import IMPClient
from .imp_platform.data_types import *
from .base.detection import Detection
from .base.segmentation import Segmentation
import argparse
import numpy as np
from tqdm import tqdm
from enum import Enum
import time
from threading import Thread
from queue import Queue
import threading
import signal
import sys
from functools import partial


def signal_handler(sig, frame, exit_flag):
    print(f'Handling signal: {signal.Signals(sig).name}')
    exit_flag.set()
    sys.exit(0)


class Backend(Enum):
    yolo = 'yolo'
    clip = 'clip'

    def __str__(self):
        return self.value


def fg_color(color):
    if np.mean(color) >= 128:
        return (0, 0, 0)
    else:
        return (255, 255, 255)
    

def is_imp_supported(cls):
    # TODO: Add filters here
    # return cls in ['person', 'bicycle', 'car', 
    #                'motorcycle', 'airplane', 'bus', 
    #                'train', 'truck']
    return True


def yolo_class_to_imp(cls):
    if cls == 'person':
        return ImageDetection.pedestrian
    elif cls in ['bicycle', 'car', 
                   'motorcycle', 'bus', 
                   'train', 'truck']:
        return ImageDetection.vehicle
    elif cls == 'traffic_light':
        return ImageDetection.traffic_light
    elif cls in ['stop sign']:
        return ImageDetection.traffic_sign


def load_gateway_vars():
    # TODO: Update these if env var names are changed by Thingspace
    ENV_API_HOST = 'MEDIA_STORE_HOST'
    ENV_API_PORT = 'MEDIA_STORE_PORT'
    ENV_ACCOUNT_ID = 'ACCOUNT_ID'
    ENV_SOURCE_ID = 'SOURCE_ID'
    ENV_APPLICATION_ID = 'APPLICATION_ID'
    media_host = os.getenv(ENV_API_HOST) if os.getenv(ENV_API_HOST) else 'http://127.0.0.1'
    media_port = os.getenv(ENV_API_PORT) if os.getenv(ENV_API_PORT) else '9090'
    account_id = os.getenv(ENV_ACCOUNT_ID) if os.getenv(ENV_ACCOUNT_ID) else 'test_acc'
    source_id = os.getenv(ENV_SOURCE_ID) if os.getenv(ENV_SOURCE_ID) else '00075fca-f8fa-faf8-ca5f-0700075fca5f'
    application_id = os.getenv(ENV_APPLICATION_ID) if os.getenv(ENV_APPLICATION_ID) else 'test_app'
    return media_host, media_port, account_id, source_id, application_id


def blended_rect(img, pt1, pt2, color, alpha):
    # From https://stackoverflow.com/a/56472613

    # First we crop the sub-rect from the image
    x1, y1 = min(pt1[0], pt2[0]), min(pt1[1], pt2[1])
    x2, y2 = max(pt1[0], pt2[0]), max(pt1[1], pt2[1])

    sub_img = img[y1:y2, x1:x2]
    rect = (np.ones(sub_img.shape) * color).astype(np.uint8)
    res = cv.addWeighted(sub_img, alpha, rect, 1 - alpha, 1.0)
    # Putting the image back to its position
    img[y1:y2, x1:x2] = res


def draw_color_legend(img, keys, colormap):
    if keys is None or len(keys) == 0:
        return
    
    fThickness = max(1, int(np.max(img.shape) / 1280))
    fScale = max(0.25, np.max(img.shape) / 1920)
    font = cv.FONT_HERSHEY_DUPLEX
    padding = 4
    row = img.shape[0]
    (w, h), baseline = cv.getTextSize(max(keys, key=len), font, fScale, fThickness)
    baseline += fThickness
    bg_box_st = [0, img.shape[0]]
    bg_box_ed = [w + h + baseline + 3*padding, row - (h + baseline + padding) * len(keys) - padding]
    blended_rect(img, bg_box_st, bg_box_ed, (60, 60, 60), 0.35)
    # cv.rectangle(img, bg_box_st, bg_box_ed, (60, 60, 60), -1, cv.LINE_AA)
    
    for k in keys:
        c = colormap[k]
        b = np.array([padding, row - h - baseline - padding, h + baseline, h + baseline])
        cv.rectangle(img, b, c, -1, cv.LINE_AA)
        text_pt = b[:2] + [h + baseline + padding, h]
        cv.putText(img, k, text_pt, font, fScale, c, fThickness, cv.LINE_AA)
        row -= h + baseline + padding


def read_frames(cap, queue, exit_flag, forward_flag, reverse_flag, skip_interval, stop_frame=None):
    total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    is_stream = total_frames <= 0

    if is_stream:
        print('[FrameThread]: Reading frames from stream')
    else:
        fps = cap.get(cv.CAP_PROP_FPS)
        delay = 1e9 / fps
        print(f'[FrameThread]: Reading frames at {fps} fps')

    while not exit_flag.is_set():
        if stop_frame and cap.get(cv.CAP_PROP_POS_FRAMES) >= stop_frame:
            print(f'[FrameThread]: Reached stop frame: {stop_frame}, stopping')
            exit_flag.set()
            break

        start_time_ns = time.process_time_ns()

        if forward_flag.is_set() or reverse_flag.is_set():
            forward = forward_flag.is_set()
            forward_flag.clear()
            reverse_flag.clear()
            cap.set(cv.CAP_PROP_POS_FRAMES, cap.get(cv.CAP_PROP_POS_FRAMES) + ((-1) ** ~forward * skip_interval))

        res, frame = cap.read()
        if not res or exit_flag.is_set():
            print('[FrameThread]: No more frames to read')
            exit_flag.set()
            break

        # Put the frame in the queue, discarding the oldest frame if necessary
        if queue.full():
            queue.get()

        queue.put(frame)

        if not is_stream:
            stop_time_ns = time.process_time_ns()
            time.sleep(max(0, delay - (stop_time_ns - start_time_ns)) / 1e9)
        
    cap.release()
    print('[FrameThread]: Exiting read_frames')


def main(args):
    video = args.video
    queries = args.text
    save_output = args.save_output
    headless = args.headless
    threaded = args.threaded
    thingspace_enabled = args.thingspace
    imp_enabled = args.imp

    video_name = os.path.splitext(os.path.basename(video))[0]
    cap = cv.VideoCapture()
    res = cap.open(video, apiPreference=cv.CAP_FFMPEG)

    if not res:
        print(f'Could not open video: {video}')
        return
    
    if args.backend == Backend.yolo:
        model = YoloDetector()
    else:
        model = CLIPDetector(queries)
        # model = CNNDetector(2)

    fps = cap.get(cv.CAP_PROP_FPS)
    frame_width, frame_height = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    isStream = total_frames <= 0

    print(f'Opened {"stream" if isStream else "video/camera"}: {video_name}, {frame_width}x{frame_height}, {fps} fps')

    if thingspace_enabled:
        gateway_client = GatewayClient(*load_gateway_vars())
        # Dummy report
        gateway_client.report_image(int(time.time()), 'security_test', 'test')

    if imp_enabled:
        imp_client = IMPClient("dummy_ip", "dummy_port")

    skip_interval = total_frames // 100 if not isStream else 10
    start_frame = args.start_frame
    start_time = args.start_time
    stop_frame = args.stop_frame
    stop_time = args.stop_time

    if start_time:
        start_frame = math.floor(fps * start_time)
    
    if stop_time:
        stop_frame = round(fps * stop_time)
    
    if not isStream:
        cap.set(cv.CAP_PROP_POS_FRAMES, start_frame)

    writer = None
    if save_output:
        out_video = f'output_{video_name}.mp4'
        writer = cv.VideoWriter(out_video, cv.VideoWriter.fourcc('m', 'p', '4', 'v'), fps, (frame_width, frame_height))

    tm = cv.TickMeter()
    pbar = tqdm(range(total_frames) if not isStream else (), desc='Frames', unit='frames')
    pbar.n = start_frame
    font = cv.FONT_HERSHEY_DUPLEX
    fThickness = max(1, int(max(frame_width, frame_height) / 1280))
    fScale = max(0.5, max(frame_width, frame_height) / 1920)
    box_colors = dict()
    label_colors = dict()
    rng = np.random.default_rng()
    contour_alpha = 0.65
    text_pos = np.array([10, 10], dtype=int)

    # Create a queue to hold the latest frame
    queue = Queue(maxsize=1)
    exit_flag = threading.Event()
    forward_flag = threading.Event()
    reverse_flag = threading.Event()

    signal.signal(signal.SIGINT, partial(signal_handler, exit_flag=exit_flag))

    # Start a thread to continuously read frames
    if threaded:
        capture_thread = Thread(target=read_frames, 
                                args=(cap, queue, exit_flag, forward_flag, reverse_flag, skip_interval, stop_frame))
        capture_thread.start()

    # Initialize Pygame
    if not headless:  
        import pygame
        import pygame.locals as pl
        wnd_name = 'C2X Test (hit ESC or Q to quit)'
        pygame.init()
        # Create a Pygame window
        screen_dims = (frame_width, frame_height)
        screen = pygame.display.set_mode(screen_dims, pygame.HWSURFACE | pygame.RESIZABLE | pygame.DOUBLEBUF)
        disp_buffer = screen.copy()
        # Set the window title
        pygame.display.set_caption(wnd_name)

    while not exit_flag.is_set():
        tstart = time.process_time()

        if threaded:
            if queue.empty():
                continue

            frame = queue.get()
        else:
            ret, frame = cap.read()
            if not ret:
                exit_flag.set()
                break

        # writer_in.write(frame)

        tm.start()
        det = model.detect(frame)
        tm.stop()

        contour_img = frame.copy()
        once = True

        for item in det:
            contour = None
            if isinstance(det, Segmentation):
                b, c, prob, contour = item
            else:
                b, c, prob = item

            if thingspace_enabled and gateway_client.is_valid() and once:
                gateway_client.report_image(tstart, 'detection_event', f'{c}: {b}')
                once = False

            if imp_enabled and imp_client.is_valid() and is_imp_supported(c):
                # TODO: Only send limited detections/when detection changes
                imp_client.send_image_detection(yolo_class_to_imp(c), DetectionExtents(*b))

            if headless and not save_output:
                continue

            if c not in box_colors:
                box_colors[c] = tuple(rng.integers(0, 255, 3).astype(float))
                label_colors[c] = fg_color(box_colors[c])

            box_color = box_colors[c]
            label_color = label_colors[c]
            (w, h), baseline = cv.getTextSize(c, font, fScale, fThickness)
            cv.rectangle(frame, b, box_color, fThickness, cv.LINE_AA)
            text_box = [b[0], b[1], max(b[2], w), h + baseline]
            cv.rectangle(frame, text_box, box_color, -1, cv.LINE_AA)
            cv.putText(frame, f'{c}, {prob:.2f}', b[:2] + [0, h], font, fScale, label_color, fThickness, cv.LINE_AA)

            if contour is not None:
                cv.drawContours(contour_img, [contour], 0, box_color, -1, cv.LINE_AA)
        
        frame = cv.addWeighted(frame, contour_alpha, contour_img, 1 - contour_alpha, 1.0)
        draw_color_legend(frame, box_colors.keys(), box_colors)

        if not headless or save_output:
            fps_text = f'Avg. inference: {tm.getAvgTimeMilli():.1f} ms'
            (w, h), baseline = cv.getTextSize(fps_text, font, fScale, fThickness)
            cv.rectangle(frame, (*text_pos, w, h + baseline), (0, 0, 0), -1, cv.LINE_4)
            cv.putText(frame, fps_text, text_pos + [0, h], font, fScale, (255, 255, 255), fThickness)

        if save_output:
            writer.write(frame)

        if not headless:
            # Convert the OpenCV image (BGR format) to a Pygame image (RGB format)
            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame_pygame = pygame.image.frombuffer(frame_rgb.tobytes(), frame_rgb.shape[1::-1], "RGB")
            # Draw the Pygame image
            # From https://stackoverflow.com/a/34919705
            # Draw to a temporary buffer and then scale it to the window size
            disp_buffer.blit(frame_pygame, (0, 0))
            screen.blit(pygame.transform.scale(disp_buffer, screen.get_size()), (0, 0))
            pygame.display.flip()

            # Event loop for Pygame
            for event in pygame.event.get():
                if event.type == pl.QUIT or (event.type == pl.KEYDOWN and (event.key == pl.K_ESCAPE or event.key == pl.K_q)):
                    exit_flag.set()
                    break
                elif event.type == pl.KEYDOWN and event.key in [pl.K_LEFT, pl.K_RIGHT]:
                    forward = event.key == pl.K_RIGHT
                    if not threaded:
                        cap.set(cv.CAP_PROP_POS_FRAMES, cap.get(cv.CAP_PROP_POS_FRAMES) + ((-1) ** ~forward * skip_interval))
                    else:
                        if forward:
                            forward_flag.set()
                        else:
                            reverse_flag.set()

                    pbar.n = int(cap.get(cv.CAP_PROP_POS_FRAMES)) - 1
                elif event.type == pygame.VIDEORESIZE:
                    # Get delta of the change in percentage of size
                    delta_w = math.fabs(event.w - screen_dims[0]) / screen_dims[0]
                    delta_h = math.fabs(event.h - screen_dims[1]) / screen_dims[1]
                    # Set new size based on which dimension changed more
                    if delta_w > delta_h:
                        new_dims = (event.w, int(event.w * frame_height / frame_width))
                    else:
                        new_dims = (int(event.h * frame_width / frame_height), event.h)

                    # Lock to image aspect ratio
                    screen = pygame.display.set_mode(new_dims, pygame.HWSURFACE | pygame.RESIZABLE | pygame.DOUBLEBUF)
                    screen_dims = new_dims

            waitTime = max(1, int((1000. / fps) - (time.process_time() - tstart)))
            time.sleep(waitTime / 1000.)

        pbar.update()

    pbar.close()
    print(f'Avg. detection time: {tm.getAvgTimeMilli()} ms')
    
    if threaded:
        capture_thread.join()
    else:
        cap.release()

    if writer:
        writer.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect objects in videos')
    parser.add_argument('-v', '--video', type=str, help='Video file', required=True)
    parser.add_argument('-t', '--text', type=str, nargs='+', help='Text queries')
    parser.add_argument('-s', '--save_output', action='store_true', help='Save output video')
    parser.add_argument('--threaded', action='store_true', help='Read video frames in a separate thread')
    parser.add_argument('-b', '--backend', type=Backend, default=Backend.yolo, 
                        help='Backend model to be used')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--thingspace', action='store_true',
                        help='Connect to Thingspace Gateway API')
    parser.add_argument('--imp', action='store_true',
                        help='Connect to IMP Client API')
    
    skip_group = parser.add_mutually_exclusive_group()
    skip_group.add_argument('--start_frame', type=int, default=0, help='Skip frames until specified index')
    skip_group.add_argument('--start_time', type=float, help='Skip frames until specified time (s)')
    
    stop_group = parser.add_mutually_exclusive_group()
    stop_group.add_argument('--stop_frame', type=int, help='Stop at specified frame index')
    stop_group.add_argument('--stop_time', type=float, help='Stop at specified time (s)')

    args = parser.parse_args()
    main(args)
