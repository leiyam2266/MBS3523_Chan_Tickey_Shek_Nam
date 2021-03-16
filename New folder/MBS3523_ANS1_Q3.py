# Save this file to your Github as OpenCV-11-Haar-face-video.py
import cv2
import numpy as np
# import turtle
from turtle import *
# import random
import random 
print(cv2.__version__)

color = random.randint(0,255)

faceCascade = cv2.CascadeClassifier('MBS3523 Resources/haarcascade_frontalface_default.xml')
cars_cascade = cv2.CascadeClassifier('MBS3523 Resources/haarcascade_car.xml')
eyeCascade = cv2.CascadeClassifier('MBS3523 Resources/haarcascade_eye.xml')

capture = cv2.VideoCapture('MBS3523 Resources/20210314_220400.mp4')
# capture = cv2.VideoCapture(0)


while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), ( color, color, color), thickness=2)
    cars = cars_cascade.detectMultiScale(img, 1.5, 6)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w,y+h), (color, color, color), thickness=2)

    cv2.imshow('Frame', img)
    #cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(1) == 32:
        break

capture.release()
cv2.destroyAllWindows()
