import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import cv2 as cv
from .models.clip_detector import CLIPDetector
from .models.yolo_detector import YoloDetector
from .base.detection import Detection
from .base.segmentation import Segmentation
import argparse
import numpy as np
from tqdm import tqdm
from enum import Enum
import time


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


def main(args):
    image_dir = args.image_dir
    out_dir = args.out_dir
    queries = args.text
    save_output = args.save_output
    headless = args.headless
    
    if not os.path.exists(image_dir):
        print(f'Error: Directory {image_dir} does not exist!')
        return
    
    img_files = []
    for _, _, files in os.walk(image_dir):
        img_files = [os.path.join(image_dir, f) for f in files]
        break

    if not out_dir or out_dir == '':
        image_dir_name = os.path.basename(os.path.normpath(image_dir))
        script_dir = os.path.dirname(__file__)
        out_dir = os.path.join(script_dir, 'out_' + image_dir_name)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if args.backend == Backend.yolo:
        model = YoloDetector()
    else:
        model = CLIPDetector(queries)
    
    if not headless:
        cv.namedWindow('Disp', cv.WINDOW_AUTOSIZE)

    tm = cv.TickMeter()
 
    font = cv.FONT_HERSHEY_DUPLEX
    box_colors = dict()
    label_colors = dict()
    rng = np.random.default_rng()
    contour_alpha = 0.65
    fps = 2
    
    for img_file in tqdm(img_files):
        tstart = time.process_time()
        img_name = os.path.splitext(os.path.basename(img_file))[0]
        img = cv.imread(img_file)
        if img is None:
            tqdm.write(f'Error: Could not read {img_name}')
            continue

        tqdm.write(f'{img_name}: {img.shape}')

        tm.start()
        det = model.detect(img)
        tm.stop()

        fThickness = max(1, int(np.max(img.shape) / 1280))
        fScale = max(0.5, np.max(img.shape) / 1920)
        leg_keys = set()

        contour_img = img.copy()

        for item in det:
            if headless and not save_output:
                continue

            contour = None
            if isinstance(det, Segmentation):
                b, c, contour = item
            else:
                b, c = item

            if c not in box_colors:
                box_colors[c] = tuple(rng.integers(50, 255, 3).astype(float))
                label_colors[c] = fg_color(box_colors[c])

            leg_keys.add(c)
            box_color = box_colors[c]
            label_color = label_colors[c]
            (w, h), baseline = cv.getTextSize(c, font, fScale, fThickness)
            cv.rectangle(img, b, box_color, fThickness, cv.LINE_AA)
            text_box = np.array([b[0], b[1], max(b[2], w), h + baseline])
            blended_rect(img, text_box[:2], text_box[2:] + text_box[:2], box_color, 0.25)
            cv.putText(img, c, b[:2] + [0, h], font, fScale, label_color, fThickness, cv.LINE_AA)
            if contour is not None:
                cv.drawContours(contour_img, [contour], 0, box_color, -1, cv.LINE_AA)
        
        img = cv.addWeighted(img, contour_alpha, contour_img, 1 - contour_alpha, 1.0)
        # if leg_keys:
        #     draw_color_legend(img, leg_keys, box_colors)

        if save_output:
            out_name = os.path.join(out_dir, 'out_' + img_name + '.png')
            cv.imwrite(out_name, img)

        if not headless:
            waitTime = max(1, int((1000. / fps) - (time.process_time() - tstart)))
            cv.imshow('Disp', img)
            k = cv.waitKeyEx(waitTime)
            if k == ord('q'):
                break

    print(f'Avg. detection time: {tm.getAvgTimeMilli()} ms')
    
    if not headless:
        cv.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect objects in images')
    parser.add_argument('-i', '--image_dir', type=str, help='Path containing images', required=True)
    parser.add_argument('-o', '--out_dir', type=str, help='Output directory')
    parser.add_argument('-t', '--text', type=str, nargs='+', help='Text queries')
    parser.add_argument('-s', '--save_output', action='store_true', help='Save output images')
    parser.add_argument('-b', '--backend', type=Backend, default=Backend.yolo, 
                        help='Backend model to be used')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')

    args = parser.parse_args()
    main(args)