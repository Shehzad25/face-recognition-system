Face Recognition System
A real-time face recognition system built with Python using the face_recognition, cv2, and os libraries. The system captures video from the webcam, detects faces, and matches them against known individuals using facial encodings.

Features
Real-time face detection and recognition.
Detects faces from video stream and labels them based on the provided dataset.
Supports the addition of custom individuals to the dataset.
Draws bounding boxes around recognized faces and labels them with the corresponding name.
Requirements
Python 3.x
OpenCV
face_recognition
os (for file operations)
You can install the required libraries by running:

bash
Copy code
pip install opencv-python face_recognition
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/face-recognition.git
Navigate to the project directory:
bash
Copy code
cd face-recognition
Install the required libraries:
bash
Copy code
pip install -r requirements.txt
Usage
Prepare the Dataset:

Create a dataset/ directory with subdirectories for each person containing their images.
Example directory structure:
Copy code
dataset/
  ├── pooja/
  ├── sneha/
  └── shehzad/
Run the Program:

Start the face recognition system by running the following command:
bash
Copy code
python face_recognition_system.py
Recognition in Real-Time:

The program will capture video from your webcam, detect faces, and attempt to recognize them based on the known dataset.
It will display the name of the recognized person on the screen. If a face is not recognized, it will be labeled as "Unknown".
Exit:

Press q to quit the video capture and close the program.
