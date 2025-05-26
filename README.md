title: "📸 Face Attendance System"
description: >
  A Python-based face recognition attendance system using OpenCV, Tkinter, and machine learning.
  Automatically marks attendance by recognizing faces through a webcam, storing attendance logs, 
  and managing datasets for training and recognition.

sections:
  - title: "✨ Features"
    list:
      - "🧑‍💻 Face Registration: Add new faces via webcam"
      - "🧠 Face Recognition: Real-time face detection and attendance marking"
      - "📊 Attendance Records: Saves logs with ID, name, date, and time (CSV)"
      - "🖥 User-Friendly GUI: Tkinter interface with functional buttons"
      - "🗂 Data Management: Stores face images and ID-name mappings"

  - title: "⚙️ Installation"
    steps:
      - "1️⃣ Clone the repository:"
      - |
        git clone https://github.com/Pranav8722/face-attendance.git
        cd face-attendance
      - "2️⃣ Install dependencies:"
      - "🟢 Python 3.x"
      - "🟢 OpenCV (`opencv-python`)"
      - "🟢 Numpy"
      - "🟢 Pandas"
      - "🟢 Pillow (for trainer)"
      - "🟢 Tkinter (usually pre-installed)"
      - "📦 Use pip:"
      - |
        pip install opencv-python numpy pandas pillow

  - title: "🚀 Usage"
    steps:
      - "🆕 Register New Faces:"
      - |
        python attendance_system.py
      - "➡️ Click 'Add Face to Dataset', enter user ID & name, webcam captures images"
      - "🧪 Train the Model:"
      - "➡️ Click 'Train Data' OR run:"
      - |
        python trainer.py
      - "📍 Mark Attendance:"
      - "➡️ Click 'Mark Attendance', face is recognized and logged"
      - "🧹 Clear Attendance:"
      - |
        python clear_attendance.py

  - title: "📁 File Structure"
    list:
      - "`attendance_system.py` — Main app (GUI)"
      - "`face_dataset.py` — Captures facial images"
      - "`trainer.py` — Trains recognizer on dataset"
      - "`clear_attendance.py` — Clears attendance log"
      - "`haarcascade_frontalface_default.xml` — Haar Cascade file"
      - "`dataset/` — Folder storing captured images"
      - "`trainer/trainer.yml` — Trained face recognition model"
      - "`attendance.csv` — Attendance record log"
      - "`id_name_mapping.csv` — Maps user ID to name"

  - title: "🧠 How It Works"
    steps:
      - "📸 Face Registration: Captures multiple images per user with unique ID"
      - "🧠 Model Training: LBPH recognizer trained on dataset"
      - "🧍‍♂️ Recognition & Attendance: Webcam detects faces, logs attendance in CSV"

  - title: "📝 Notes"
    list:
      - "💡 Use good lighting for better recognition accuracy"
      - "📷 Default: 30 images per user during registration"
      - "🛠 GUI is customizable for advanced features"

  - title: "📜 License"
    content: >
      This project is open-source and available under the MIT License.

  - title: "🙏 Acknowledgements"
    list:
      - "[OpenCV](https://opencv.org/)"
      - "[Tkinter GUI Library](https://docs.python.org/3/library/tkinter.html)"
