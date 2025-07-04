import cv2
import dlib
import numpy as np
import pygame  # For sound alert
from scipy.spatial import distance
from plyer import notification  


pygame.mixer.init()


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)


cap = cv2.VideoCapture(0)

EYE_AR_THRESH = 0.25  
EYE_AR_CONSEC_FRAMES = 20  
counter = 0
alarm_playing = False  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    drowsy = False
    EAR_value = 0

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(42, 48)])
        right_eye = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(36, 42)])

        left_EAR = eye_aspect_ratio(left_eye)
        right_EAR = eye_aspect_ratio(right_eye)
        EAR_value = (left_EAR + right_EAR) / 2.0

        if EAR_value < EYE_AR_THRESH:
            counter += 1
            if counter >= EYE_AR_CONSEC_FRAMES and not alarm_playing:
                # Play alarm
                pygame.mixer.music.load("alarm.mp3")  
                pygame.mixer.music.play()
                alarm_playing = True
                drowsy = True

                
                notification.notify(
                    title="Drowsiness Alert!",
                    message="You seem drowsy. Please take a break!",
                    app_icon=None,  
                    timeout=5
                )
        else:
            counter = 0  
            if alarm_playing:
                pygame.mixer.music.stop()
                alarm_playing = False

        
        for (x, y) in np.concatenate((left_eye, right_eye), axis=0):
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    
    h, w, _ = frame.shape

    
    if drowsy:
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, h), (0, 0, 255), -1)
        cv2.addWeighted(overlay, 0.3, frame, 0.7, 0, frame)

        cv2.putText(frame, "ALERT! DROWSINESS DETECTED", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    
    cv2.rectangle(frame, (0, h - 50), (w, h), (50, 50, 50), -1)  

    
    cv2.putText(frame, f"EAR: {EAR_value:.2f}", (20, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    
    cv2.putText(frame, "Press 'Q' to exit", (w - 200, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow("Drowsiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
