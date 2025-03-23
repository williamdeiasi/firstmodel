import os
import cv2
from ultralytics import YOLO

# === Set VOC 2012 image path === #
voc_images_path = "data/data/VOCdevkit/VOC2012/JPEGImages/"  # Enter your path, this is example
output_path = "output_voc/"  # Folder to save annotated images

# === Make sure output directory exists === #
os.makedirs(output_path, exist_ok=True)

# === Load YOLOv8 model === #
model = YOLO("yolov8n.pt")  # Use yolov8s.pt or yolov8m.pt for better accuracy

# === Get a list of images === #
image_files = sorted([f for f in os.listdir(voc_images_path) if f.endswith('.jpg')])

# === Process each image === #
for idx, image_file in enumerate(image_files[:10]):  # Run on first 10 images
    image_path = os.path.join(voc_images_path, image_file)
    frame = cv2.imread(image_path)

    if frame is None:
        print(f"Warning: Failed to load {image_path}")
        continue

    # Run YOLO detection
    results = model(frame)

    # Process detected objects
    for result in results:
        boxes = result.boxes.xyxy  # Bounding box coordinates
        scores = result.boxes.conf  # Confidence scores
        classes = result.boxes.cls  # Class labels

        num_boxes = len(boxes)  # Automatically use the number of detected objects

        print(f"\nImage {image_file} - Detected {num_boxes} Objects:")
        for i in range(num_boxes):
            print(f"  Object {i+1}:")
            print(f"    Bounding Box: {boxes[i].tolist()}")
            print(f"    Confidence: {scores[i].item():.2f}")
            print(f"    Class: {int(classes[i].item())}")

    # Annotate frame with detected objects
    annotated_frame = frame.copy()
    for i in range(num_boxes):
        x1, y1, x2, y2 = map(int, boxes[i])
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{int(classes[i].item())}: {scores[i].item():.2f}"
        cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save annotated image
    output_file_path = os.path.join(output_path, image_file)
    cv2.imwrite(output_file_path, annotated_frame)

    # Display image (optional)
    cv2.imshow("YOLO VOC Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print(f"\nAnnotated images saved in '{output_path}'")
