import numpy as np
import cv2
import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from flask import Flask

cur_face = int(0)
total_face = int(0)
cnt = 0
ans = 0
max_people = 0

def nothing():
    pass
def start_cascade():
    global ans, cnt, total_face, max_people
    face_cascade = cv2.CascadeClassifier('/home/yong/e_commercial/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while 1:

        cnt = cnt + 1
        if(cnt > 100):
            break
        
        ret, img = cap.read()
        cur_face = 0

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        faces = face_cascade.detectMultiScale(gray, 1.2, 4)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cur_face = cur_face + 1
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        total_face = total_face + cur_face
        max_people = max(max_people, cur_face)
        cv2.imshow('img',img)
        print("The number of detected people are " + str(cur_face) + " " + str(cnt))    
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break


    ans = total_face / cnt
    retouch()
    cap.release()
    cv2.destroyAllWindows()

    
def retouch():
    global ans
    global max_people
    for i in range(1, 20):
        if ans * (1 + (i/10)) < max_people:
            ans = ans * (1+(i/10))





start_cascade()
retouch()

app = Flask(__name__)
@app.route('/')
def index():
    global ans, max_people
    return "최소 대기인원 : " + str(round(ans, 2)) + '<br>' + "최대 대기인원 : " + str(max_people)

app.run()