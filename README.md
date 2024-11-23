# Facial Detection App

A modern facial detection application that identifies faces in uploaded images or through a webcam feed. This app uses AI-powered algorithms to recognize and highlight faces in real-time.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Contact](#contact)

---

## Overview

The Facial Detection App is a web-based application that uses advanced computer vision techniques to detect faces. Users can upload an image or enable their webcam for real-time face detection.

## Features

- Detects faces in images and live webcam feeds
- Highlights detected faces with bounding boxes

## Technologies Used

- **Frontend:** HTML
- **AI/ML Integration:**OpenCV
- **Deployment:** Yet to be done

## Setup and Installation

- How to use :
- Download IP camera app from google playstore : [IP Camera](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN)
- Start the server from the app by clicking on the 3-dots above. This will return you the url for ip address for streaming your ip camera
- to use the ip camera, change the camera_path variable in WebcamApi.py file with the url of ip address of the ip camera. Make sure that your camera and device are connected to the same network(A fast wifi is recommended to stream the image). also ensure to add the "/video" at the end of your server url path.

## Contact

Thanks to [btwGaurav](https://github.com/btwGaurav) for adding an amazing Readme.

Happy Development !
