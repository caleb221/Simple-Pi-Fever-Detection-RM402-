Hello!
This is a standalone IoT (Internet of Things) web app that connects users to a live feed of an Infrared Camera.


It also attempts to take the user's temperature and inform them if they have a fever


A small scale study accompanied this project with users feedback concerning the usability of the device.
# Images






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
  
Thanks for looking at my code!
-Caleb
