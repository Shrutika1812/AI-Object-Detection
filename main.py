
import cv2
from ultralytics import YOLO

# Load the AI model
model = YOLO("yolo11n.pt")

# Open your laptop's webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("AI Object Detection Started!")
print("Press 'q' to stop.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read webcam.")
        break

    # Detect objects using AI
    results = model(frame)

    # Display detected objects and their labels
    annotated_frame = results[0].plot()

    cv2.imshow("AI Object Detection", annotated_frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
