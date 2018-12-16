import os
import math
import time

import busio
import json
import numpy as np
#import pygame
from scipy.interpolate import griddata
import board
from colour import Color


import adafruit_amg88xx

i2c_bus = busio.I2C(board.SCL, board.SDA)

#low range of the sensor (this will be blue on the scr16een)
MINTEMP = 20.

#high range of the sensor (this will be red on the screen)
MAXTEMP =30.

#how many color values we can have
COLORDEPTH = 300 #300

os.putenv('SDL_FBDEV', '/dev/fb1')
#pygame.init()

#initialize the sensor
sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

# pylint: disable=invalid-slice-index
points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]
# pylint: enable=invalid-slice-index

#sensor is an 8x8 grid so lets do a square
height = 240
width = 240

#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))

#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

displayPixelWidth = width / 30
displayPixelHeight = height / 30

#lcd = pygame.display.set_mode((width, height))

#lcd.fill((255, 0, 0))

#pygame.display.update()
#pygame.mouse.set_visible(False)

#lcd.fill((0, 0, 0))
#pygame.display.update()

#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def diagnosis(temp):
	#print(len(temp))
	tempArr=np.array(temp)
	#avg = np.average(temp)
	#print(avg)
	#ERASE ALL VALUES LOWER THAN NUMBER
	zeroedOut=np.where(tempArr > room_temperature)
	#print(tempArr[zeroedOut])
	actuallyHot = tempArr[zeroedOut]
	avg = np.average(actuallyHot)
	if np.isnan(avg):
		avg = "Please step into the view of Camera"
	elif avg >norm:
		avg = str(float(avg+2.5))+" You might be a little sick"
	elif avg <norm:
		avg = str(float(avg+2.5))+"\n you appear normal"
	elif avg<40:
		avg="Please step back"
        
	
	#print(avg)
	return avg

# INDICES OF DSIRE VALUES:
#goodvalues = [3, 4, 7]
# ix = np.isin(x, goodvalues)
#
#
#let the sensor initialize
time.sleep(.1)

#========================================
room_temperature = 25
norm=29
#========================================
c=[ ['' for x in range(32)]  for y  in range(32) ]
jsonX= [ k for k in range(32) ]
jsonY=jsonX
while True:

    #read the pixels
    pixels = []
#    start = time.time()
    for row in sensor.pixels:
        pixels = pixels + row
    pixels = [map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
    tot_avg=diagnosis(sensor.pixels)
    #perform interpolation
    bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
    #colorVal=[]
#   print(colors)
    #draw everything
    for ix, row in enumerate(bicubic):
        for jx, pixel in enumerate(row):
            t = colors[constrain(int(pixel), 0, COLORDEPTH- 1)]
            tc = '#%02x%02x%02x' % t
            #print(t)
            c[ix][jx]=tc
    #print(c)
    #save the data and send to server

    jsonData= {"square": {"len":32,"x":
                jsonX,"y":jsonY,"color":c},"temp":tot_avg}
    with open("sensorData.json","w+") as f:
        json.dump(jsonData,f)
 #   now = time.time()
 #   procTime=now-start
 #   print(procTime)
#    time.sleep(.01)
    #pygame.display.update()
    #values:
    # pixels
    # blue.hex <-- JSON FILE TO BE SAVED AND PASSED:
    # { object .value object. color
    # }
    #
    # draw colors across 8X8 grid 
    #

   # pygame.image.save(lcd,"outputPicture.png")
    
