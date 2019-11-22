import numpy as np
import cv2
from flask import Flask
from multiprocessing import Process

cnt_face = int(3)

app = Flask(__name__)

@app.route('/')
def main():
    return str(cnt_face)

face_cascade = cv2.CascadeClassifier('/home/yong/e_commercial/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

def func1():
    print("aaaa")
    app.run()
    print("bbbb")

def func2():
    while 1:
        cnt_face = 0
        ret, img = cap.read()
        

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cnt_face = cnt_face + 1
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        cv2.imshow('img',img)
        print("The number of detected people : ", cnt_face)    
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            return

        cap.release()
        cv2.destroyAllWindows()

def func3():
    while(1):
        cnt_face = 10
        
p1 = Process(target=func1)
p2 = Process(target=func2)

p1.start()
p2.start()

p1.join()
p2.join()