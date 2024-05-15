import cv2
from ultralytics import YOLO
from ultralytics.utils.checks import check_imshow
from ultralytics.utils.plotting import Annotator, colors
from collections import defaultdict
from utils import check_paths

# Load the model
model = YOLO('models/best_helmet.pt')

# Load the image
image_path = 'input/images.jpeg'
image = cv2.imread(image_path)
image = cv2.resize(image, (640, 480))

# Check if the image was correctly loaded
assert image is not None, 'Cannot load image'

# Perform inference
results = model(image)
annotated = results[0].plot()

cv2.imshow('Annotated', annotated)
cv2.waitKey(0)