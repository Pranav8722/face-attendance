import cv2
import numpy as np
import pandas as pd
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

# Global variables
attendance_recorded = set()
face_id = 0

def record_attendance(id, name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not os.path.exists('attendance.csv'):
        df = pd.DataFrame(columns=['ID', 'Name', 'Date', 'Time'])
    else:
        df = pd.read_csv('attendance.csv')

    df = pd.concat([df, pd.DataFrame([{'ID': id, 'Name': name, 'Date': date, 'Time': time}])], ignore_index=True)
    df.to_csv('attendance.csv', index=False)

def save_id_name_mapping(id, name):
    if not os.path.exists('id_name_mapping.csv'):
        df = pd.DataFrame(columns=['ID', 'Name'])
    else:
        df = pd.read_csv('id_name_mapping.csv')

    if df[df['ID'] == int(id)].empty:
        df = pd.concat([df, pd.DataFrame([{'ID': int(id), 'Name': name}])], ignore_index=True)
        df.to_csv('id_name_mapping.csv', index=False)

def get_name_from_id(id):
    if not os.path.exists('id_name_mapping.csv'):
        return "Unknown"

    df = pd.read_csv('id_name_mapping.csv')
    person = df[df['ID'] == int(id)]
    if not person.empty:
        return person.iloc[0]['Name']
    else:
        return "Unknown"

def train_data():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    def get_images_and_labels(path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        ids = []
        for image_path in image_paths:
            face_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces.append(face_img)
            ids.append(int(os.path.split(image_path)[-1].split(".")[1]))
        return faces, ids
    
    dataset_path = 'dataset'
    faces, ids = get_images_and_labels(dataset_path)
    
    recognizer.train(faces, np.array(ids))
    recognizer.write('trainer/trainer.yml')
    
    print("Training completed successfully.")

def add_face():
    global face_id
    
    id = simpledialog.askstring("Input", "Enter ID:")
    if id is None:
        return
    name = simpledialog.askstring("Input", "Enter Name:")
    if name is None:
        return
    
    save_id_name_mapping(id, name)
    
    cam = cv2.VideoCapture(0)
    cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            face_id += 1
            filename = f"dataset/User.{id}.{face_id}.jpg"
            cv2.imwrite(filename, gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.waitKey(100)
        
        cv2.imshow('camera', img)
        cv2.waitKey(1)
        
        if face_id >= 30:
            break
    
    cam.release()
    cv2.destroyAllWindows()

def recognize_face():
    global attendance_recorded
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    cam = cv2.VideoCapture(0)
    
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        
        for (x, y, w, h) in faces:
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            
            if confidence < 50:  # Adjust threshold as needed
                name = get_name_from_id(id)
                confidence_text = f"  {round(100 - confidence)}%"
                if id not in attendance_recorded:
                    record_attendance(id, name)
                    attendance_recorded.add(id)
            else:
                id = "."
                name = "unknown"
                confidence_text = f"  {round(100 - confidence)}%"
            
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, f"{id} - {name}", (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence_text), (x+5, y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)
        
        cv2.imshow('camera', img)
        
        if cv2.waitKey(10) & 0xFF == 27:
            break
    
    cam.release()
    cv2.destroyAllWindows()

def mark_attendance():
    try:
        recognize_face()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app.quit()

def train_and_add_faces():
    train_data()
    add_face()

app = tk.Tk()
app.title("Attendance System")

mark_btn = tk.Button(app, text="Mark Attendance", command=mark_attendance)
mark_btn.pack(pady=10)

train_btn = tk.Button(app, text="Train Data", command=train_and_add_faces)
train_btn.pack(pady=10)

add_face_btn = tk.Button(app, text="Add Face to Dataset", command=add_face)
add_face_btn.pack(pady=10)

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
