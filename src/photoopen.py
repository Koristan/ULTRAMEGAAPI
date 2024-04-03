import shutil
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Load a model
model = YOLO('src/best.pt')  # pretrained YOLOv8n model
# Run batched inference on a list of images

def get_boxes (image):
    
    model.predict(image, conf=0.7, save=True, save_txt=True, show_labels=True)
    labels = list()
    
    results = model([image])
    
    
    try:
        for r in results:
            boxes = r.boxes
            names = r.names
            for box in boxes:           
                     
                classe = names[int(round(box.cls.item()))]
                x1 = int(round(box.xyxy.numpy()[0][0]))
                y1 = int(round(box.xyxy.numpy()[0][1]))
                x2 = int(round(box.xyxy.numpy()[0][2]))
                y2 = int(round(box.xyxy.numpy()[0][3]))
            
                labels.append((classe, x1, y1, x2, y2))
                
    except Exception as e:
        print(f"WARNING: {e}")
    
    return labels