import torch
import cv2 as cv
from PIL import Image
import requests
import numpy as np
from transformers import CLIPProcessor, CLIPModel
import time
import sys
from pathlib import Path
import pickle
import os

import cv2
import numpy as np
import subprocess
from streamlink import Streamlink
import ffmpeg
import threading
import multiprocessing
import math
from sklearn import preprocessing

from .imp_platform.imp_client import IMPClient
from .imp_platform.data_types import *

# CamList = ['NCAM001', 'NCAM006', 'NCAM223', 'NCAM159', 'NCAM204', 'NCAM167', 'SCAM144', 'NCAM197', 'NCAM209',
#            'NCAM088', 'KCAM001', 'KCAM174', 'SCAM199', 'SCAM170', 'KCAM129', 'KCAM110',
#            'KCAM170', 'KCAM180', 'KCAM027', 'KCAM086', 'KCAM004', 'KCAM162', 'KCAM028', 'KCAM029', 'KCAM030',
#            'SCAM213','SCAM182','SCAM012','SCAM003','PCAM4061','SCAM144','SCAM011','SCAM208','SCAM177','SCAM014','SCAM194']


#CamList = ['NCAM001', 'NCAM006',
 #       'data/out_truck.mp4',
 #         'NCAM159', 'data/nighttime_2.mp4',
  #         'data/fog_SCAM003_20240507-051038.mp4',
   #        'NCAM204', 'NCAM167', 'data/traffic_KCAM030_20240507-103904.mp4','SCAM144', 'NCAM197', 'NCAM209',
   #       'NCAM088', 'KCAM001', 'KCAM174', 'SCAM199', ] #'SCAM170' #'KCAM129', 'KCAM004']
#

         #'KCAM170', 'KCAM180', 'KCAM027', 'KCAM086', 'KCAM110', 'KCAM162', 'KCAM028', 'KCAM029', 'KCAM030']
#CamList = ['NCAM001', 'NCAM006','KCAM001', 'KCAM174','data/out_CCTVtruck.mp4']
CamList = ['data/out_CCTVtruck.mp4', 'data/nighttime_2.mp4', 'data/fog_SCAM011_20240507-033640.mp4']
#CamList = ['data/nighttime_2.mp4']
# CamList = ['KCAM001', 'KCAM174']
# CamList = ['PCAM4061']
# 'https://video.deldot.gov/live/KCAM174.stream/playlist.m3u8'

headless = False
exit_flag, ui_flag, streams_loaded_flag, IMP_flag = False, False, False, False
aspect_wide, aspect_tall, scl = 580, 650, 1.0
vid_h = aspect_tall
compos_h, compos_w, mgn, dx = int(vid_h * scl), int(1080 * scl), 5, int(np.ceil(math.sqrt(len(CamList))))
preview_h, preview_w = compos_h // dx - mgn, compos_w // dx - mgn
head_top, head_left = int(compos_h*0.1), preview_w+mgn+int(compos_h*0.1)
compos_w += head_left
compos_h += head_top
compos = np.zeros((compos_h, compos_w, 3), dtype=np.uint8)
compos_frames = [None]*pow(dx,2)
list_lock = threading.Lock()
inference_w, inference_h = 224, 224
record_w, record_h, record_fps = 480, 320, 5
# alert_queries = ['traffic','flood','fog','accident','truck','bus','RV','pedestrian','bicycle']
# alert_queries = ['traffic','flood','fog','accident','truck','bus','RV','bicycle']
alert_queries = ['traffic','traffic congestion', 'flood','fog','accident','vehicle crash','explosion']
#alert_queries += ['stop sign violation', 'red light violation', 'car going wrong way']
# alert_queries = ['bus']
logo_texts = ['delaware department text', 'sorry camera not available']
alert_exclude = ['highway','road'] + logo_texts
alert_queries = alert_queries + alert_exclude
alert_thresh = 0.8

col_red = (50, 50, 235)
col_orange = (50, 100, 200)
col_blue = (235, 50, 50)
col_highlight = col_orange
col_frozen = col_blue
col_loading = (185,185,185)
col_text = (205, 205, 205)
col_shadow = (25, 25, 25)
global imp_client

def clip_class_to_imp(cls):
    print('**************** {} *******', cls)
    if cls == 'vehicle crash':
        return IncidentsName.accident
    elif cls == 'explosion':
        return IncidentsName.explosion
    elif cls == 'fog':
        return IncidentsName.fogwarning
    elif cls == 'traffic congestion':
        return IncidentsName.congestion
    else:
        return IncidentsName.notmatching

def clip_class_to_camera(cls):
    print('**************** {} *******', cls)
    if cls == 'vehicle crash':
        return "CAM1"
    elif cls == 'explosion':
         return "CAM2"
    elif cls == 'fog':
        return "CAM3"
    elif cls == 'traffic congestion':
        return "CAM4"
    elif cls == 'traffic congestion':
        return "None"
    else:
        return "None"

def callback_alert_first_detected(label_short, label_long):
    global IMP_flag
    IMP_flag = True
    print(label_short)
    print(label_long)
    value1 = clip_class_to_imp(format(label_short))
    camera = clip_class_to_camera(format(label_short))
    imp_client.send_incident_detection(value1, camera)
    print('Send message to IMP: {} '.format(label_long))


def ensure(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

def resize_aspect(img, height):
    h, w = img.shape[:2]
    aspect = w / h
    resized = cv2.resize(img, (int(height * aspect), height), interpolation=cv2.INTER_AREA)
    return resized

def resize_vid(tgt_w, tgt_h, image, letterbox=False):
    if letterbox:
        ratio = (tgt_w / image.shape[1]) if image.shape[0] * tgt_w / image.shape[1] < tgt_h else (tgt_h / image.shape[0])
    else:
        ratio = (tgt_w / image.shape[1]) if image.shape[0] * tgt_w / image.shape[1] > tgt_h else (tgt_h / image.shape[0])
    res_h, res_w = int(image.shape[0] * ratio), int(image.shape[1] * ratio)
    resized = cv2.resize(image, None, None, ratio, ratio, interpolation=cv2.INTER_AREA)
    M = np.eye(3, dtype=np.float32)
    M[0, 2] = tgt_w // 2 - res_w // 2
    M[1, 2] = tgt_h // 2 - res_h // 2
    resized = cv2.warpPerspective(resized, M, (tgt_w, tgt_h))
    return resized

class ddot_lock(object):
    def __init__(self):
        self.fname_lock = 'out_ddot4/lock.txt'

    def __enter__(self):
        while os.path.exists(self.fname_lock):
            time.sleep(0.01)

        with open(self.fname_lock, 'w') as f:
            f.write('lock for all_embeddings.pkl')

    def __exit__(self, *args):
        os.remove(self.fname_lock)

def draw_text(img, text, pos, scale=1., color=col_text):
    cv2.putText(img, text, (pos[0], int(pos[1]+scl*20)), cv2.FONT_HERSHEY_PLAIN, scl*2*scale, col_shadow, int(scl+1)*3)
    cv2.putText(img, text, (pos[0], int(pos[1]+scl*20)), cv2.FONT_HERSHEY_PLAIN, scl*2*scale, color, int(scl+1))


def get_loading_data(unresponsive=False):
    loading = np.zeros((preview_h, preview_w, 3), dtype=np.uint8)
    cv2.rectangle(loading, (int(preview_w * 1 / 4), int(preview_h * 1 / 4)), (int(preview_w * 3 / 4), int(preview_h * 3 / 4)), col_loading, mgn)
    if unresponsive:
        cv2.rectangle(loading, (int(preview_w * 1 / 4), int(preview_h * 1 / 4)), (int(preview_w * 3 / 4), int(preview_h * 3 / 4)), col_red, mgn)
    loading_data = {'f_preview': loading,
                      'f_inf': None,
                      'time': time.time()}
    return loading_data

def process_stream(CamID, idx):
    global compos_frames, exit_flag, streams_loaded_flag
    if 'data/' in CamID:
        url = CamID
        from_file = True
    else:
        url = 'https://video.deldot.gov/live/{}.stream/playlist.m3u8'.format(CamID)
        from_file = False
    while True:
        print('starting: {}'.format(idx))
        with list_lock:
            compos_frames[idx] = None
        cap = cv.VideoCapture()
        res = cap.open(url, apiPreference=cv.CAP_FFMPEG)
        with list_lock:
            compos_frames[idx] = get_loading_data()
        if not res:
            time.sleep(1)
            continue
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        stream_fps = float(cap.get(cv2.CAP_PROP_FPS))
        frame_idx = 0
        while True:
            if from_file and not streams_loaded_flag:
                time.sleep(1)
                continue
            t0 = time.time()
            if frame_idx%500==0:
                print('reading: {}'.format(idx))
            res, frame = cap.read()
            if not res and not from_file:
                break
            elif not res and from_file:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            r_preview = resize_vid(preview_w, preview_h, frame)
            r_inf = resize_vid(inference_w, inference_h, frame)
            r_record = resize_vid(record_w, record_h, frame)
            with list_lock:
                alert_timeout = int(stream_fps * 60)
                if 'alert' in compos_frames[idx] and compos_frames[idx]['alert']['frame_ix'] >= alert_timeout:
                    compos_frames[idx].pop('alert')
                if 'alert' in compos_frames[idx]:
                    alert_text = compos_frames[idx]['alert']['label']
                    alert_text_short = compos_frames[idx]['alert']['label_short']
                    compos_frames[idx]['alert']['frame_ix']+=1
                else:
                    alert_text = None
                    alert_text_short = None
            if alert_text_short is not None:
                alert_frame = r_record
                # cv2.rectangle(alert_frame, (0, 0), (record_w, record_h), col_highlight, mgn)
                draw_text(alert_frame, alert_text, (mgn, mgn), scale=0.3)
            with list_lock:
                compos_frames[idx].update({'f_preview': r_preview,
                                           'f_inf': r_inf,
                                           'time': time.time(),
                                           'from_file': from_file,
                                           })
            t_loop = time.time()-t0
            if 1/stream_fps > t_loop:
                time.sleep((1/stream_fps-t_loop)/2)
            if exit_flag:
                break
            frame_idx+=1

        print('shutting down: {}'.format(idx))
        with list_lock:
            compos_frames[idx].update(get_loading_data())
        cap.release()
        if exit_flag:
            break

def process_preview():
    global compos_frames, exit_flag, streams_loaded_flag, IMP_flag
    if headless:
        return
    ix_preview = 0
    out = cv2.VideoWriter('./output_ddot_demo.mp4', cv2.VideoWriter_fourcc(*'vp09'), 5, (compos.shape[1], compos.shape[0]))
    while True:
        with list_lock:
            compos_frames_cpy = compos_frames

        draw_time = time.time()
        compos[:,:,:] = 0
        ix_alert = 0
        num_loaded = 0
        for i_f in range(len(CamList)):
            if compos_frames_cpy[i_f] is None:
                continue
            num_loaded+=1
            x_pos = (i_f % dx) * (preview_w + mgn) + head_left
            y_pos = (i_f // dx) * (preview_h + mgn) + head_top
            if draw_time-compos_frames_cpy[i_f]['time'] > 2:
                cv2.rectangle(compos_frames_cpy[i_f]['f_preview'], (0, 0), (preview_w, preview_h), col_frozen, mgn)
            compos[y_pos:y_pos + preview_h, x_pos:x_pos + preview_w, :] = compos_frames_cpy[i_f]['f_preview']
            if 'alert' in compos_frames_cpy[i_f] and ix_alert<dx and compos_frames_cpy[i_f]['from_file']:
                x_pos = mgn
                y_pos = (ix_alert) * (preview_h + mgn) + head_top
                compos[y_pos:y_pos + preview_h, x_pos:x_pos + preview_w, :] = compos_frames_cpy[i_f]['f_preview']
                cv2.rectangle(compos, (x_pos, y_pos), (x_pos+preview_w, y_pos+preview_h), col_highlight, int(mgn/2))
                if draw_time - compos_frames_cpy[i_f]['time'] > 2:
                    cv2.rectangle(compos, (x_pos, y_pos), (x_pos + preview_w, y_pos + preview_h), col_frozen, int(mgn/2))
                draw_text(compos, compos_frames_cpy[i_f]['alert']['label'], (x_pos+mgn, y_pos+mgn), scale=0.6)
                ix_alert+=1

        if num_loaded>=int(len(CamList)*0.8):
            streams_loaded_flag = True
        pos_txt_alerts = (mgn*2, mgn*2)
        pos_txt_cameras = (head_left+mgn*2, mgn*2)
        draw_text(compos, 'Alerts:', pos_txt_alerts)
        draw_text(compos, 'Cameras:', pos_txt_cameras)
        # if (ix_preview // 90) % 2 == 0:
        #     cv2.rectangle(compos, pos_txt_alerts, (pos_txt_alerts[0]+mgn*70,pos_txt_alerts[1]+mgn*10), col_text, mgn)
        #     cv2.rectangle(compos, pos_txt_cameras, (pos_txt_cameras[0]+mgn*70,pos_txt_cameras[1]+mgn*10), col_text, mgn)
        if IMP_flag:
            pos_txt_imp = (mgn * 2 + 180, mgn * 2+10)
            draw_text(compos, 'IMP SENT', pos_txt_imp, scale=1.25, color=col_highlight)

        if not exit_flag and streams_loaded_flag:
            out.write(compos)
        cv2.imshow('Ddot stream', compos)
        k = cv2.waitKey(int(1000/30))
        ix_preview+=1
        if k == ord('q'):
            out.release()
            exit_flag = True
        if ui_flag:
            break


def process_inference():
    global compos_frames, exit_flag, streams_loaded_flag
    assert (torch.cuda.is_available())
    device = torch.device("cuda")
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    with ddot_lock():
        all_embeddings, fname_embeddings = torch.zeros((0, 512)).to(device), 'out_ddot4/all_embeddings.pkl'
        all_embeddings = all_embeddings if not os.path.exists(fname_embeddings) else pickle.load(open(fname_embeddings, 'rb'))
        embeddings_index, fname_index = {'byidx': {}, 'byfname': {}}, 'out_ddot4/embeddings_index.pkl'
        embeddings_index = embeddings_index if not os.path.exists(fname_index) else pickle.load(open(fname_index, 'rb'))
    while True:
        with list_lock:
            compos_frames_cpy = compos_frames
        inf_time, inf_frames, inf_idx, inf_fps = time.time(), [], [], 5
        for i_f in range(len(CamList)):
            if compos_frames_cpy[i_f] is None or compos_frames_cpy[i_f]['f_inf'] is None:
                continue
            if inf_time-compos_frames_cpy[i_f]['time'] < 2:
                img_rgb = cv.cvtColor(compos_frames_cpy[i_f]['f_inf'], cv.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img_rgb)
                inf_frames.append(img_pil)
                inf_idx.append(i_f)
        if inf_frames:
            inputs = processor(text=alert_queries, images=inf_frames, return_tensors="pt", padding=True).to(device)
            outputs = model(**inputs)
            if True:
                probs = outputs.logits_per_image.softmax(dim=1)
                best_idx = probs.argmax(dim=1)
                with list_lock:
                    for i_prob in range(probs.shape[0]):
                        prob_f = probs[i_prob,best_idx[i_prob].item()].item()
                        if prob_f > alert_thresh and alert_queries[best_idx[i_prob].item()] not in alert_exclude and streams_loaded_flag:
                            label = '{} {:.2f}'.format(alert_queries[best_idx[i_prob].item()], prob_f)
                            label_short = alert_queries[best_idx[i_prob].item()]
                            i_f = inf_idx[i_prob]
                            if 'alert' not in compos_frames[i_f] and compos_frames[i_f]['from_file'] and streams_loaded_flag:
                                callback_alert_first_detected(label_short, label)
                            compos_frames[i_f]['alert'] = {'label': label, 'label_short': label_short, 'time': time.time(), 'frame_ix': 0}
            else:
                qry_e = outputs.text_embeds / torch.linalg.norm(outputs.text_embeds)
                srch_e = outputs.image_embeds / torch.linalg.norm(outputs.image_embeds)
                qry_e1 = torch.from_numpy(preprocessing.normalize(outputs.text_embeds.detach().cpu().numpy(), norm='l2')).to(device)
                srch_e1 = torch.from_numpy(preprocessing.normalize(outputs.image_embeds.detach().cpu().numpy(), norm='l2')).to(device)
                ac1 = torch.allclose(qry_e, qry_e1)
                ac2 = torch.allclose(srch_e, srch_e1)
                all_similarity = torch.matmul(srch_e, qry_e.T)
                similarity_max = all_similarity.max(dim=1)
                all_similarity1 = torch.matmul(srch_e1, qry_e1.T)
                similarity_max1 = all_similarity1.max(dim=1)
                similarity_max = similarity_max1
                with list_lock:
                    for i_prob in range(similarity_max.values.shape[0]):
                        prob_f = similarity_max.values[i_prob].item()
                        if prob_f > alert_thresh:
                            label = '{} {:.2f}'.format(alert_queries[similarity_max.indices[i_prob].item()], prob_f)
                            label_short = alert_queries[similarity_max.indices[i_prob].item()]
                            i_f = inf_idx[i_prob]
                            compos_frames[i_f]['alert'] = {'label': label, 'label_short': label_short, 'time': time.time(), 'frame_ix': 0}

        time.sleep(1/inf_fps)
        if exit_flag:
            break


if __name__ == "__main__":
    imp_enabled = True

    imp_client = IMPClient("127.0.0.1", "dummy_port")

    stream_threads = []
    thread_preview = threading.Thread(target=process_preview, args=())
    thread_preview.start()
    thread_inference = threading.Thread(target=process_inference, args=())
    thread_inference.start()


    for c_idx, CamID in enumerate(CamList):
        thread = threading.Thread(target=process_stream, args=(CamID, c_idx))
        thread.start()
        stream_threads.append(thread)

    while True:
        with list_lock:
            compos_frames_cpy = compos_frames

        main_time = time.time()
        for i_f in range(len(CamList)):
            if compos_frames_cpy[i_f] is None:
                continue
            if main_time - compos_frames_cpy[i_f]['time'] > 60*5:
                with list_lock:
                    compos_frames[i_f].update(get_loading_data(unresponsive=True))
                if 'stream_recorder' in compos_frames_cpy[i_f]:
                    compos_frames_cpy[i_f]['stream_recorder'].release()
                    compos_frames_cpy[i_f]['alert_recorder'].release()
                #
                # stream_threads[i_f].terminate()
                # stream_threads[i_f].join()
                # stream_threads[i_f] = threading.Thread(target=process_stream, args=(CamID, c_idx))
                # stream_threads[i_f].start()

        time.sleep(1)
        if exit_flag:
            break

    thread_inference.join()
    for thread in stream_threads:
        thread.join()

    ui_flag = True
    thread_preview.join()
    cv2.destroyAllWindows()


