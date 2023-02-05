# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:45:24 2023

@author: HP
"""


from flask import Flask, render_template, Response
import cv2

GREEN = (0, 255, 0)

app = Flask(__name__)

'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''



face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")



def face_data(image):

    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    x_coordinate = 0
    y_coordinate = 0
    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), GREEN, 2)
        face_width = w
        x_coordinate = x
        y_coordinate = y-10

    return (face_width, x_coordinate, y_coordinate)





ref_image = cv2.imread("Sample_8.jpg")
ref_image_face_width = face_data(ref_image)[0]

camera = cv2.VideoCapture(0)


def gen_frames():  
    while True:
        success, frame = camera.read()
        
        face_width_in_frame = face_data(frame)[0]
        face_x_coordinate = face_data(frame)[1]
        face_y_coordinate = face_data(frame)[2]
        
        if not success:
            break
        
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)