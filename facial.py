import cv2
import mediapipe as mp
import time

face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
alien_w , alien_h = 640,480
cap.set(3, alien_w)
cap.set(4, alien_h)
frame= 100
l_delay = 1

while True:
     ret, img=cap.read()
     img=cv2.flip(img,1)
     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     faces=face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30,30)
    )

     for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+frame,y+frame),(0,255,255),2)
     cv2.putText(img, 'image obtainedkyg,j ',(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,255),2)
     cv2.imshow('Face detection',img)
     cv2.waitKey(1)