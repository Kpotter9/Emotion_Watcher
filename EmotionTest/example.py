"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from deepface import DeepFace


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it

    text = ""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(rgb_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]

        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']
        emotion_confidences = result[0]['emotion']
        my_confidence = ""
        # Print each emotion with its confidence
        for emo, confidence in emotion_confidences.items():
            if emo == emotion:
                my_confidence = str(round(confidence, 2))
            print(f"{emo}: {confidence:.2f}%")
        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        gaze.refresh(face_roi)

        text = ""

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"
        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        if right_pupil:
            cv2.line(frame, (right_pupil[0] + x + 5, right_pupil[1] + y), (right_pupil[0] + x - 5, right_pupil[1] + y),(255, 100, 100), 2)
            cv2.line(frame, (right_pupil[0] + x, right_pupil[1] + y + 5), (right_pupil[0] + x, right_pupil[1] + y - 5),(255, 100, 100), 2)
        if left_pupil:
            cv2.line(frame,(left_pupil[0]+x+5,left_pupil[1]+y),(left_pupil[0]+x-5,left_pupil[1]+y),(255,100,100),2)
            cv2.line(frame,(left_pupil[0]+x,left_pupil[1]+y+5),(left_pupil[0]+x,left_pupil[1]+y-5),(255,100,100),2)

        cv2.putText(frame, emotion + " " + my_confidence, (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        if gaze.horizontal_ratio():
            cv2.putText(frame, text+" "+f"{gaze.horizontal_ratio()*100: .2f}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27 or not cv2.getWindowProperty("Demo",cv2.WND_PROP_VISIBLE)>=1:
        break
   
webcam.release()
cv2.destroyAllWindows()
