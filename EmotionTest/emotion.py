
import cv2
import time
from deepface import DeepFace

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame

    ret, frame = cap.read()

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]


        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
        # Determine the dominant emotion
        emotion= result[0]['dominant_emotion']
        emotion_confidences = result[0]['emotion']
        my_confidence=""
        # Print each emotion with its confidence
        for emo, confidence in emotion_confidences.items():
            if emo==emotion:
                my_confidence=str(round(confidence,2))
            print(f"{emo}: {confidence:.2f}%")
        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion+" "+my_confidence, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    # Display the resulting frame
    cv2.imshow('Real-time Emotion Detection', frame)

    if cv2.waitKey(1) & (0xFF == ord('q')or cv2.getWindowProperty('Real-time Emotion Detection', cv2.WND_PROP_VISIBLE) < 1):
        break




