Hello!


This is a standalone IoT (Internet of Things) web app that connects users to a live feed of an Infrared Camera.


It also attempts to take the user's temperature and inform them if they have a fever


A small scale study accompanied this project with users feedback concerning the usability of the device.
The user Simply Scans a QR Code in order to access the device. (while connected to university WiFi)

If you would like the whole paper writeup of this project including results and further discussion, I would be happy to share it, just send an email!
# Images
Raspberry Pi and Infrared Camera


<img src = "https://github.com/caleb221/Simple-Pi-Fever-Detection-RM402-/blob/master/Img/physicalPic.jpg"   height="200" width="220">


Web App


<img src = "https://github.com/caleb221/Simple-Pi-Fever-Detection-RM402-/blob/master/Img/normalUI.png"   height="300" width="200">


Flow Chart for whole System


<img src = "https://github.com/caleb221/Simple-Pi-Fever-Detection-RM402-/blob/master/Img/SfFC_color.png" height="500" width="290">

# Pre-requesite libraries:
Python:


    -busio
     -json
    -numpy
    -scipy
    -board
    -colour
    -adafruit_amg88xx
    -glob,matplotlib (STATISTICS PROGRAM ONLY)
JavaScript:
  
  
     -express
     -socket.io
     -pyshell
  
  
Here is a basic overview to what each code does.

# SensorRandom.py

this code is the interface between sensor and raspberry pi.    
it updates a JSON file as quickly as it can (~.3ms) with the colors for the web page
as well as the diagnosis. 

(sorry about the name, its not actually random. I wrote a random data generator before I had the sensor and didn't want to clutter my file system.)
# pythonNode.js
Javascript function to run the python code sensorRandom while running the web server.
# router.js
client side server. This listens on a local port 8001 and serves the web app UI. It sends the JSON file from the pi to the user every time the file is updated (~.3ms).
# main.js
a simple main function that runs both router and pythonNode simultaneously.
# index.html
   just as the name suggests, this is the main UI for the webapp, it draws the JSON data on a canvas
   using javascript as well as shows the user their diagnosis.
# feedBack.html
Questionnaire used in a tiny reasearch project to collect user data concerning the webapp.
# feedBack_stats.py 
Statistical analysis done on feedback data for a class. Papers and whatnot are elsewhere, this is a code section.

Thanks for looking at my code!
-Caleb
