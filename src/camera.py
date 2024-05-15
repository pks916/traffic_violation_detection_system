import os
import numpy as np
import cv2
from ultralytics import YOLO
from ultralytics.utils.checks import check_imshow
from ultralytics.utils.plotting import Annotator, colors

from collections import defaultdict

from utils import check_paths

cap = cv2.VideoCapture("input/vdo.mp4")
model = YOLO('models/best_helmet.pt')
image = 'input/images.jpeg'
# tripling_model = YOLO('models/tripling_violation.pt')

# w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

assert cap.isOpened(), 'Cannot capture Video'

check_paths()
track_history = defaultdict(lambda: [])
names = model.model.names

ctr=0

while True:
    
    ret, frame = cap.read()
    if not ret:
        print('-----------------------------------STREAM ENDED-----------------------------------')
        break

    # resize frame to HD resolution
    original_frame = frame
    frame = cv2.resize(frame, (1980, 1080))

    if ctr%5==0:
        results = model.track(frame, persist=True, verbose=False, imgsz=(640,640), conf=0.4, device='cpu')
        annotated = results[0].plot()
        
        if results[0].boxes.id is not None:
            clss = results[0].boxes.cls.cpu().tolist()
            track_ids = results[0].boxes.id.int().tolist()
            boxes = results[0].boxes.xyxy.int().cpu().tolist()

            for box, cls, track_id in zip(boxes, clss, track_ids):
                track = track_history[track_id]

                track.append([cls, box])
                if len(track) > 1:
                    track.pop(0)
            
            print(track_history.items())

        cv2.imshow("YOLOv8 Tracking", annotated)
    ctr+=1

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()