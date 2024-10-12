from gaze_tracking import GazeTracking
from deepface import DeepFace
import cv2
class Scan(object):
    def __init__(self):
        self.gaze = GazeTracking()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.emotion_data=[0,0,0,0,0,0,0]
        self.faces=0
        self.attention=0




    def get_scan(self,webcam):
        # We get a new frame from the webcam
        frame: object
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it

        text = ""
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert grayscale frame to RGB format
        rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

        # Detect faces in the frame
        faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        count_head=0
        self.emotion_data=[0,0,0,0,0,0,0]
        self.faces=0
        for (x, y, w, h) in faces:
            count_head+=1
            # Extract the face ROI (Region of Interest)
            face_roi = rgb_frame[y:y + h, x:x + w]

            # Perform emotion analysis on the face ROI
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            # Determine the dominant emotion
            emotion = result[0]['dominant_emotion']
            emotion_confidences = result[0]['emotion']
            my_confidence = ""
            # Print each emotion with its confidence
            i=0
            print(emotion_confidences.items())



            for emo, confidence in emotion_confidences.items():
                if emo == emotion:

                    my_confidence = str(round(confidence, 2))
                #print(f"{emo}: {confidence:.2f}%")
                if emo == "angry":
                    self.emotion_data[0] = confidence
                elif emo == "disgust":
                    self.emotion_data[1] = confidence
                elif emo == "fear":
                    self.emotion_data[2] = confidence
                elif emo == "happy":
                    self.emotion_data[3] = confidence
                elif emo == "sad":
                    self.emotion_data[4] = confidence
                elif emo == "surprise":
                    self.emotion_data[5] = confidence
                elif emo == "neutral":
                    self.emotion_data[6] = confidence




            # Draw rectangle around face and label with predicted emotion
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            self.gaze.refresh(face_roi)


            self.attention+=100-((abs(self.gaze.horizontal_ratio()-50))*2)

            text = ""

            if self.gaze.is_blinking():
                text = "Blinking"
            elif self.gaze.is_right():
                text = "Looking right"
            elif self.gaze.is_left():
                text = "Looking left"
            elif self.gaze.is_center():
                text = "Looking center"
            left_pupil = self.gaze.pupil_left_coords()
            right_pupil = self.gaze.pupil_right_coords()
            if right_pupil:
                cv2.line(frame, (right_pupil[0] + x + 5, right_pupil[1] + y),
                         (right_pupil[0] + x - 5, right_pupil[1] + y), (255, 100, 100), 2)
                cv2.line(frame, (right_pupil[0] + x, right_pupil[1] + y + 5),
                         (right_pupil[0] + x, right_pupil[1] + y - 5), (255, 100, 100), 2)
            if left_pupil:
                cv2.line(frame, (left_pupil[0] + x + 5, left_pupil[1] + y), (left_pupil[0] + x - 5, left_pupil[1] + y),
                         (255, 100, 100), 2)
                cv2.line(frame, (left_pupil[0] + x, left_pupil[1] + y + 5), (left_pupil[0] + x, left_pupil[1] + y - 5),
                         (255, 100, 100), 2)

            cv2.putText(frame, emotion + " " + my_confidence, (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),
                        2)
            if self.gaze.horizontal_ratio():
                cv2.putText(frame, text + " " + f"{self.gaze.horizontal_ratio() * 100: .2f}", (x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        self.frame=frame
        self.faces=count_head
        if self.faces>0:
            for i in range(7):
                self.emotion_data[i]=self.emotion_data[i]/self.faces
            self.attention=self.attention/self.faces
        return count_head
