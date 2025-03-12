<<<<<<< HEAD
import os
import shutil

# Paths
mot17_path = "C:/Users/William/model1/MOT17/train"
yolo_images_path = "../datasets/MOT17_YOLO/images/train"
yolo_labels_path = "../datasets/MOT17_YOLO/labels/train"

# Ensure output directories exist
os.makedirs(yolo_images_path, exist_ok=True)
os.makedirs(yolo_labels_path, exist_ok=True)

# Function to convert MOT17 format to YOLO
def convert_annotation(mot_file, yolo_file):
    with open(mot_file, "r") as f:
        lines = f.readlines()

    with open(yolo_file, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if len(data) < 7:
                continue  

            class_id = 0  
            x, y, w, h = map(float, data[2:6])
            x_center, y_center = x + w / 2, y + h / 2

            # 
            x_center /= 1920
            y_center /= 1080
            w /= 1920
            h /= 1080

            f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")

# Convert all MOT17 annotations
for seq in os.listdir(mot17_path):
    seq_path = os.path.join(mot17_path, seq, "img1")
    label_file = os.path.join(mot17_path, seq, "gt", "gt.txt")

    if os.path.exists(seq_path) and os.path.exists(label_file):
        yolo_label_file = os.path.join(yolo_labels_path, f"{seq}.txt")
        convert_annotation(label_file, yolo_label_file)

        # Copy images to the YOLO dataset
        for img in os.listdir(seq_path):
            src = os.path.join(seq_path, img)
            dst = os.path.join(yolo_images_path, img)
            shutil.copy(src, dst)

print("MOT17 annotations converted to YOLO format")
=======
import os
import shutil

# Paths
mot17_path = "C:/Users/William/model1/MOT17/train"
yolo_images_path = "../datasets/MOT17_YOLO/images/train"
yolo_labels_path = "../datasets/MOT17_YOLO/labels/train"

# Ensure output directories exist
os.makedirs(yolo_images_path, exist_ok=True)
os.makedirs(yolo_labels_path, exist_ok=True)

# Function to convert MOT17 format to YOLO
def convert_annotation(mot_file, yolo_file):
    with open(mot_file, "r") as f:
        lines = f.readlines()

    with open(yolo_file, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if len(data) < 7:
                continue  

            class_id = 0  
            x, y, w, h = map(float, data[2:6])
            x_center, y_center = x + w / 2, y + h / 2

            # 
            x_center /= 1920
            y_center /= 1080
            w /= 1920
            h /= 1080

            f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")

# Convert all MOT17 annotations
for seq in os.listdir(mot17_path):
    seq_path = os.path.join(mot17_path, seq, "img1")
    label_file = os.path.join(mot17_path, seq, "gt", "gt.txt")

    if os.path.exists(seq_path) and os.path.exists(label_file):
        yolo_label_file = os.path.join(yolo_labels_path, f"{seq}.txt")
        convert_annotation(label_file, yolo_label_file)

        # Copy images to the YOLO dataset
        for img in os.listdir(seq_path):
            src = os.path.join(seq_path, img)
            dst = os.path.join(yolo_images_path, img)
            shutil.copy(src, dst)

print("MOT17 annotations converted to YOLO format")
>>>>>>> 123fbc93ac81d847bca73e96b3039c5582416e0f
