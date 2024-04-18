import shutil
import numpy as np
from ultralytics import YOLO

from norfair.camera_motion import MotionEstimator

# Load a model
model = YOLO('src/best.pt')  # pretrained YOLOv8n model
# Run batched inference on a list of images

def get_boxes (image, tracker, motion_estimator):
    
    labels = list()
    
    
    results = model.track([image], persist=True)
    detections = detector(image)
    coord_transformations = motion_estimator.update(image)
    tracked_objects = tracker.update(detections=detections)
    
    print('GOVNO\n\n' + tracked_objects)
    
    try:
        for r in results:
            boxes = r.boxes
            names = r.names

            for box in boxes:         
                
                acc = box.conf.item()

                
                if (acc > 0.5):
                    classe = names[int(round(box.cls.item()))]
                    x1 = int(round(box.xyxy.numpy()[0][0]))
                    y1 = int(round(box.xyxy.numpy()[0][1]))
                    x2 = int(round(box.xyxy.numpy()[0][2]))
                    y2 = int(round(box.xyxy.numpy()[0][3]))
                
                    labels.append((classe, x1, y1, x2, y2))
                
    except Exception as e:
        print(f"WARNING: {e}")
    
    return labels