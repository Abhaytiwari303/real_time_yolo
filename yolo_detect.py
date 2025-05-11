import cv2
from ultralytics import YOLO

# Load video
video_path = 'video_input/bengaluru_street.mp4'
cap = cv2.VideoCapture(video_path)

# Load YOLOv8 model (you can choose nano, small, medium, etc.)
model = YOLO('yolov8n.pt')

# Video writer settings
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output/labeled_output.mp4', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO prediction
    results = model(frame)[0]
    
    # Annotate frame
    annotated_frame = results.plot()
    
    # Write frame
    out.write(annotated_frame)

    # Optional: display real-time
    cv2.imshow("YOLOv8 - Bengaluru Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
