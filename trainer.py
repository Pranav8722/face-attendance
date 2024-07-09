import cv2
import numpy as np
from PIL import Image
import os

# Path to the dataset directory
path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.startswith('.')]
    face_samples = []
    ids = []
    
    for image_path in image_paths:
        img = Image.open(image_path).convert('L')  # Convert it to grayscale
        img_numpy = np.array(img, 'uint8')
        id = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        
        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)
            print(f"Detected face in {image_path}")
    
    return face_samples, ids

print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces, ids = get_images_and_labels(path)
print(f"Detected {len(faces)} faces")

# Train the recognizer
recognizer.train(faces, np.array(ids))

# Ensure the 'trainer' directory exists
trainer_dir = 'trainer'
if not os.path.exists(trainer_dir):
    os.makedirs(trainer_dir)

# Save the trained model into the 'trainer' directory
recognizer.write(os.path.join(trainer_dir, 'trainer.yml'))  # Save the model into trainer.yml
print(f"\n [INFO] {len(np.unique(ids))} faces trained. Exiting Program")
