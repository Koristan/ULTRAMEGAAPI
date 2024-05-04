import shutil
import numpy as np

from PIL import Image

def get_boxes (image, model, tracker):
    
    labels = list()
    
    detections = model(image)[0]
    results = []
    
    try:
        
        names = detections.names
        
        for data in detections.boxes.data.tolist():
            
            confidence = data[4]
            
            if float(confidence) < 0.3:
                continue
            
            
            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            class_id = int(data[5])
                
            results.append([[xmin, ymin, xmax - xmin, ymax - ymin], confidence, class_id])
            
    except Exception as e:
        print(f"WARNING: {e}")
    
    
    tracks = tracker.update_tracks(results, frame=image)
    
    i = 0
    for track in tracks:

        track_id = track.track_id
        ltrb = track.to_ltrb()

        xmin, ymin, xmax, ymax = int(ltrb[0]), int(ltrb[1]), int(ltrb[2]), int(ltrb[3])
        
        
        labels.append([
            names[int(results[i][2])], xmin, ymin, xmax, ymax, track_id
        ])
        
        i += 1
    
    return labels