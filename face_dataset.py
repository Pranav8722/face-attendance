import cv2
import os

# Prompt user to enter a unique ID for the face being recorded
face_id = input('Enter user ID: ')

# Load the Haar cascade file for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create dataset directory if it doesn't exist
if not os.path.exists('dataset'):
    os.makedirs('dataset')

# Start video capture from the default camera (0)
cam = cv2.VideoCapture(0)
count = 0

while True:
    ret, img = cam.read()  # Read a frame from the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces in the frame
    
    for (x, y, w, h) in faces:
        count += 1
        # Save the captured face image in the dataset directory
        face_img_path = f"dataset/User.{face_id}.{count}.jpg"
        cv2.imwrite(face_img_path, gray[y:y+h, x:x+w])
        print(f"Saved {face_img_path}")
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('image', img)  # Display the frame with the rectangle
    # Break the loop if 'ESC' is pressed or if 30 images are taken
    if cv2.waitKey(100) & 0xFF == 27:
        break
    elif count >= 30:
        break

cam.release()
cv2.destroyAllWindows()
