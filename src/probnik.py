import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("src/best.pt")

# Open the video file
video_path = "C:\\test\\cam1_30fps.avi"
cap = cv2.VideoCapture(video_path)

c = 0
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        c += 1
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        boxes = results[0].boxes.xywh
        track_ids = results[0].boxes.id

        
        if track_ids is None:
            continue
        else:
            print("number of frame: ", c)
            for element in boxes:
                print(element.tolist())
            print(track_ids.tolist())

    else:
        # Break the loop if the end of the video is reached
        break
