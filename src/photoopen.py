import shutil
import numpy as np
<<<<<<< Updated upstream
from norfair import Detection

def get_boxes (image, model, tracker, motion_estimator):
    
    labels = list()
    
    results = model(image)
    norfair_detections = list()
    
    coord_transformations = motion_estimator.update(image)

    try:
        for r in results:
            boxes = r.boxes
            names = r.names  
            
            for box in boxes:         
                
                acc = box.conf.item()
                
                if (acc > 0.5):
                    
                    bbox = np.array(
                    [
                        [box.xyxy.numpy()[0][0], box.xyxy.numpy()[0][1]],
                        [box.xyxy.numpy()[0][2], box.xyxy.numpy()[0][3]],
                    ]
                    )
                    
                    scores = np.array(
                        [acc]
                    )
                    
                    norfair_detections.append(
                        Detection(
                            points=bbox,
                            scores=scores,
                            label=int(box.cls.item()),
                        )
                    )
                    tracked_objects = tracker.update(
                        detections=norfair_detections,
                        coord_transformations=coord_transformations # pass the estimation to the tracker
                    )
                    print(tracked_objects)
                    classe = names[int(round(box.cls.item()))]
                    x1 = int(round(box.xyxy.numpy()[0][0]))
                    y1 = int(round(box.xyxy.numpy()[0][1]))
                    x2 = int(round(box.xyxy.numpy()[0][2]))
                    y2 = int(round(box.xyxy.numpy()[0][3]))
                
                    labels.append((classe, x1, y1, x2, y2))
=======

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
>>>>>>> Stashed changes
                
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