import os
import time
import uuid

import cv2
from ultralytics import YOLO

new_frame_time = 0
prev_frame_time = 0
curr_frame = 0
last_helmet_frame = 0
last_overloading_frame = 0

cap = cv2.VideoCapture("traffic.mp4")
bike_model = YOLO('bike_plate_helmet.pt')
tripling_model = YOLO('tripling_violation.pt')

if not cap.isOpened():
    print('Error opening video file')
    exit(0)

if not os.path.exists('no_helmets'):
    os.makedirs('no_helmets')

if not os.path.exists('overloading'):
    os.makedirs('overloading')    

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # resize frame to HD resolution
    frame = cv2. resize(frame, (1280, 720))

    # fps calculation
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time
    fps = str(int(fps))
    cv2.putText(frame, f'FPS: {fps}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    #current frame number
    curr_frame += 1
    
    helmet = bike_model.predict(frame, imgsz=1280)
    overloading = tripling_model.predict(frame, imgsz=1280)

    # detects overloading of 2 wheeler and saves image
    for r1,r2 in zip(overloading,helmet):
        for bxs1, bxs2 in zip(r1.boxes.data, r2.boxes.data):
            if bxs1[5] == 1:
                if curr_frame - last_overloading_frame >= 25:
                    cv2.imwrite(f'overloading/{uuid.uuid1()}.png', frame)
                    last_overloading_frame = curr_frame 

            if bxs2[5] == 3:
                if curr_frame - last_helmet_frame >= 25:
                    cv2.imwrite(f'no_helmets/{uuid.uuid1()}.png', frame)
                    last_helmet_frame = curr_frame
                
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()