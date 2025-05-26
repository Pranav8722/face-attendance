project:
  name: "📸 Face Attendance System"
  description: >
    A Python-based face recognition attendance system using OpenCV, Tkinter, and machine learning.
    It automates attendance marking by recognizing faces via webcam and records logs with timestamps.
    Includes a GUI for dataset management, training, and real-time recognition.

features:
  - "🧑‍💼 Face Registration: Capture new faces using the webcam and store them with a unique ID."
  - "🤖 Face Recognition: Recognize faces in real-time and mark attendance automatically."
  - "🗓️ Attendance Logging: Save records with ID, name, date, and time in CSV format."
  - "🖼️ GUI Interface: Clean and simple GUI built with Tkinter."
  - "🗂️ Dataset Management: Maintains ID-name mappings and facial image datasets."

installation:
  prerequisites:
    - "🐍 Python 3.x"
    - "📦 pip (Python package installer)"
  dependencies:
    - "📚 opencv-python"
    - "📚 numpy"
    - "📚 pandas"
    - "📚 pillow"
    - "📚 tkinter (usually pre-installed)"
  steps:
    - step: "📥 Clone the repository"
      command: |
        git clone https://github.com/Pranav8722/face-attendance.git
        cd face-attendance
    - step: "📦 Install required packages"
      command: |
        pip install opencv-python numpy pandas pillow

usage:
  - action: "🚀 Run the application"
    command: |
      python attendance_system.py
    description: "Launches the main GUI interface."
  - action: "➕ Register New Faces"
    description: >
      Click 'Add Face to Dataset', enter user ID and name, and capture images using webcam.
  - action: "🧠 Train the Model"
    description: >
      Click 'Train Data' in the GUI or run `python trainer.py` to train the LBPH recognizer.
  - action: "📸 Mark Attendance"
    description: >
      Use 'Mark Attendance' in the GUI to recognize and log attendance into `attendance.csv`.
  - action: "🧹 Clear Attendance Logs"
    command: |
      python clear_attendance.py
    description: "Reset attendance records by clearing the log."

file_structure:
  - "📁 attendance_system.py: Main GUI application"
  - "📁 face_dataset.py: Captures new facial images"
  - "📁 trainer.py: Trains the face recognition model"
  - "🧹 clear_attendance.py: Clears attendance logs"
  - "🔍 haarcascade_frontalface_default.xml: Face detection classifier"
  - "📂 dataset/: Stores user face images"
  - "📂 trainer/trainer.yml: Saved face recognizer model"
  - "📄 attendance.csv: Attendance records"
  - "📄 id_name_mapping.csv: User ID to name mappings"

how_it_works:
  - step: "🧑‍💼 Face Registration"
    detail: "Captures 30 images per user and stores them in the dataset with a unique ID."
  - step: "🧠 Model Training"
    detail: "Trains a Local Binary Pattern Histogram (LBPH) recognizer on collected facial images."
  - step: "🕵️‍♂️ Real-Time Recognition"
    detail: "Recognizes faces via webcam and logs attendance with timestamp."

notes:
  - "💡 Use well-lit environments for accurate detection."
  - "📸 Capture multiple angles of a user’s face during registration."
  - "🔧 The system is modular and customizable for further expansion."

license:
  name: "📝 MIT License"
  type: "Open Source"
  url: "https://opensource.org/licenses/MIT"

acknowledgements:
  - name: "🔬 OpenCV"
    url: "https://opencv.org/"
  - name: "🖼️ Tkinter (Python GUI)"
    url: "https://docs.python.org/3/library/tkinter.html"
