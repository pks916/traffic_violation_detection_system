import cv2
from easyocr import Reader

cap = cv2.VideoCapture("input/traffic.mp4")

def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def ocr(frame):

    # OCR the input image using EasyOCR
    reader = Reader(['en'], gpu=False)
    results = reader.readtext(frame)
    print(results)


while True:

    ret, frame = cap.read()
    if not ret:
        print('-----------------------------------STREAM ENDED-----------------------------------')
        break

    # resize frame to HD resolution
    frame = cv2.resize(frame, (1088, 736))
    ocr(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break