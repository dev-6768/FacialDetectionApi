# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:45:24 2023

@author: HP
"""


from flask import Flask, render_template, Response, request
import cv2
from cv2 import VideoCapture, imencode, IMWRITE_JPEG_QUALITY

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_argument(r'user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data')                                             #(r"--user-data-dir=C:\Users\HP\AppData\Local\Google\Chrome\User Data\Default")
# options.add_argument('--window-size=1920,1080')
# options.add_argument(r'--profile-directory=Profile 13')
# options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
# options.add_argument("--headless")

# PATH = 'chromedriver'
# driver = webdriver.Chrome(PATH, options=options)
# driver.get("http://192.168.0.183:8080")
# wait = WebDriverWait(driver, 600)
# print("driver request found.")

# GREEN = (0, 255, 0)

# javac_xpath = '/html/body/div[5]/div[1]/div/form/div[1]/div/label[5]'

# javac_box = wait.until(EC.presence_of_element_located((
#     By.XPATH, javac_xpath)))

# javac_box.click()

# led_xpath = '/html/body/div[6]/div[4]/div[2]/form/div[7]/div/div/label[2]'

# led_box = wait.until(EC.presence_of_element_located((
#     By.XPATH, led_xpath)))

# front_xpath = '/html/body/div[6]/div[4]/div[2]/form/div[8]/div/div[2]'

# front_box = wait.until(EC.presence_of_element_located((
#     By.XPATH, front_xpath)))

app = Flask(__name__)

'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''

haarcascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
camera_path = "http://192.168.29.225:8080/video"
saved_image_path = "Sample_8.jpg"

face_detector = cv2.CascadeClassifier(haarcascade_path)

def face_data(image):

    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    x_coordinate = 0
    y_coordinate = 0
    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
        face_width = w
        x_coordinate = x
        y_coordinate = y-10

    return (face_width, x_coordinate, y_coordinate)

ref_image = cv2.imread(saved_image_path)
ref_image_face_width = face_data(ref_image)[0]

camera = VideoCapture(camera_path)


def gen_frames():  
    while True:
        success, frame = camera.read()
        
        frame_data=face_data(frame)
        
        face_width_in_frame = frame_data[0] #replace frame_data with face_data if not working.
        face_x_coordinate = frame_data[1]
        face_y_coordinate = frame_data[2]
        
        if not success:
            break
        
        else:
            encode_param = [int(IMWRITE_JPEG_QUALITY), 10]
            ret, buffer = imencode('.jpg', frame, encode_param)
            frame = buffer.tobytes()
            print(frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

@app.route('/', methods=["GET", "POST"])
def index():
    #if(request.method=="POST"):
        #led_box.click()
            
    return render_template('frame.html')

@app.route('/camera', methods=["GET", "POST"])
def cameraFunction():
    #if(request.method=="POST"):
        #front_box.click()
    
    return render_template("frame.html")
    
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)