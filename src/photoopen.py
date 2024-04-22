import shutil
import numpy as np
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
                
    except Exception as e:
        print(f"WARNING: {e}")
    
    return labels