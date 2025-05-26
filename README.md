project:
  name: "Face Attendance System"
  description: >
    A Python-based face recognition attendance system leveraging OpenCV, Tkinter, and machine learning.
    This system automates attendance tracking by recognizing faces through a webcam interface and stores
    attendance logs in a structured format. It includes user-friendly GUI components and supports real-time
    face registration, training, and attendance marking.

features:
  - "Face Registration: Capture new faces using a webcam and store them in a dataset."
  - "Face Recognition: Recognize and verify faces in real-time to mark attendance."
  - "Attendance Logging: Automatically logs attendance with ID, name, date, and timestamp in a CSV file."
  - "Graphical Interface: Intuitive GUI built with Tkinter for streamlined interaction."
  - "Dataset Management: Supports persistent mapping of user IDs to names and maintains image data."

installation:
  prerequisites:
    - "Python 3.x"
    - "pip (Python package installer)"
  dependencies:
    - "opencv-python"
    - "numpy"
    - "pandas"
    - "pillow"
    - "tkinter (usually pre-installed with Python)"
  instructions:
    - step: "Clone the repository"
      command: |
        git clone https://github.com/Pranav8722/face-attendance.git
        cd face-attendance
    - step: "Install the required packages"
      command: |
        pip install opencv-python numpy pandas pillow

usage:
  - action: "Run the GUI application"
    command: |
      python attendance_system.py
    description: "Launches the main application interface."
  - action: "Register New Faces"
    description: >
      Select 'Add Face to Dataset' in the GUI. Enter user ID and name when prompted. 
      The system will capture facial images via webcam.
  - action: "Train the Model"
    description: >
      Click 'Train Data' from the GUI or run `python trainer.py` to train the face recognition model.
  - action: "Mark Attendance"
    description: >
      Use 'Mark Attendance' to start webcam recognition. Detected faces will be verified and logged into attendance.csv.
  - action: "Clear Attendance Logs"
    command: |
      python clear_attendance.py
    description: "Clears all existing attendance records."

file_structure:
  - "attendance_system.py: Main application interface (GUI)"
  - "face_dataset.py: Captures and stores user face images"
  - "trainer.py: Trains the face recognizer model using LBPH"
  - "clear_attendance.py: Resets attendance logs"
  - "haarcascade_frontalface_default.xml: Haar cascade classifier for face detection"
  - "dataset/: Directory for storing captured facial images"
  - "trainer/trainer.yml: Serialized trained model"
  - "attendance.csv: CSV file storing attendance logs"
  - "id_name_mapping.csv: CSV file mapping user IDs to names"

how_it_works:
  - step: "Face Registration"
    detail: "Captures multiple images (default: 30) for each user, associated with a unique ID."
  - step: "Model Training"
    detail: "Uses Local Binary Pattern Histogram (LBPH) algorithm to train the face recognizer on the dataset."
  - step: "Face Recognition & Attendance"
    detail: >
      Uses the trained model to identify users in real-time via webcam and log attendance entries
      with precise timestamps.

notes:
  - "Ensure proper lighting during face registration and recognition for optimal accuracy."
  - "Multiple images per user enhance the robustness of face recognition."
  - "The GUI is modular and can be extended with reporting tools or database integration."

license:
  name: "MIT License"
  type: "Open Source"
  url: "https://opensource.org/licenses/MIT"

acknowledgements:
  - name: "OpenCV"
    url: "https://opencv.org/"
  - name: "Tkinter (Python GUI)"
    url: "https://docs.python.org/3/library/tkinter.html"
