# 여기서는 얼굴인식 코드랑 app코드가 동시에 실행이 안돼서 문제가 발생함. 하나끝나고
# 하나가 실행이 된다.

import numpy as np
import cv2
from flask import Flask
app = Flask(__name__)
cnt_face = int(0)

@app.route('/')
def main():
    return str(cnt_face)


def nothing():
    pass

# cv2.namedWindow("Scale Track Bar")
# cv2.createTrackbar('a', 'Scale Track Bar', 0, 30, nothing)
# cv2.createTrackbar('b', 'Scale Track Bar', 0, 30, nothing)
# cv2.setTrackbarPos('a', 'Scale Track Bar', 3)
# cv2.setTrackbarPos('b', 'Scale Track Bar', 10)

face_cascade = cv2.CascadeClassifier('/home/yong/e_commercial/haarcascade_frontalface_default.xml')
# body_cascade = cv2.CascadeClassifier('/home/yong/e_commercial/full_body.xml')
# uBody_cascade = cv2.CascadeClassifier('/home/yong/e_commercial/upper_body.xml')

cap = cv2.VideoCapture(0)
app.run()

# cnt_body = 0


while 1:
    # w = cv2.getTrackbarPos('a', 'Scale Track Bar')
    # h = cv2.getTrackbarPos('b', 'Scale Track Bar')
    cnt_face = 0
    # cnt_body = 0
    ret, img = cap.read()
    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # bodies = body_cascade.detectMultiScale(gray, 1.1, 10)
    # u_bodies = uBody_cascade.detectMultiScale(gray, 1.1, h)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cnt_face = cnt_face + 1
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    # for (x,y,w,h) in bodies:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    #     cnt_body = cnt_body + 1
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = img[y:y+h, x:x+w]
    
    # for (x,y,w,h) in u_bodies:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #     cnt_body = cnt_body + 1
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = img[y:y+h, x:x+w]


    cv2.imshow('img',img)
    print("The number of detected people are ", cnt_face)    
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
