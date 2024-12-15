import cv2
# import numpy as np
import face_recognition


# Load known faces and encodings
def load_known_faces():
    # Load and encode known faces
    pooja_image = face_recognition.load_image_file("dataset/pooja/WhatsApp Image 2024-10-19 at 14.29.30_c507b937.jpg")
    pooja_encoding = face_recognition.face_encodings(pooja_image)[0]
    
    sneha_image = face_recognition.load_image_file("dataset/sneha/WhatsApp Image 2024-10-19 at 14.30.08_04d5bf4c.jpg")
    sneha_encoding = face_recognition.face_encodings(sneha_image)[0]

    shehzad_image = face_recognition.load_image_file("dataset/shehzad/my.jpg")
    shehzad_encoding = face_recognition.face_encodings(shehzad_image)[0]
    
    known_encodings = [pooja_encoding, sneha_encoding,shehzad_encoding]
    known_names = ["Pooja", "Sneha","Shehzad"]
    
    return known_encodings, known_names

# Process each video frame and recognize faces
def process_frame(frame, known_encodings, known_names):
    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame, model='hog')  # Use 'hog' for speed
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    # Compare faces and label recognized ones
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.6)  # Adjust tolerance
        name = "Unknown"
        match_index = -1
        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]
        
        # Print the index and name
        print(f"Matched index: {match_index}, Name: {name}")
        
        # Draw rectangle and label around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({match_index})", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    
    # Return the processed frame
    return frame

# Main function to start video stream and process each frame
def main():
    # Load known faces and encodings
    known_encodings, known_names = load_known_faces()
    
    # Start video capture from webcam
    video_capture = cv2.VideoCapture(0)  # 0 is the default webcam
    
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        
        # If frame was captured successfully
        if ret:
            # Process the frame
            processed_frame = process_frame(frame, known_encodings, known_names)
            
            # Display the resulting frame
            cv2.imshow('Face Recognition', processed_frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()

# Run the program
if __name__ == "__main__":
    main()
