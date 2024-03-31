import shutil
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Load a model
model = YOLO('src/best.pt')  # pretrained YOLOv8n model
# Run batched inference on a list of images

def get_boxes (image):
    
    model.predict(image, conf=0.7, save=True, save_txt=True, show_labels=True)
    
    results = model([image])
    classes = results[0].names
    labels = list()
    try:
        with open('runs/detect/predict/labels/image0.txt', 'r') as f:
            file = f.read()
            
            file = file.split('\n')
            
            for row in file:
                
                row = row.split(' ')
                
                classe = classes[int(0)]
                x1 = row[1]
                y1 = row[2]
                x2 = row[3]
                y2 = row[4]
                
                labels.append((classe, x1, y1, x2, y2))
                
    except Exception as e:
        print(f"WARNING: {e}")
        
    shutil.rmtree('runs')
    
    return labels