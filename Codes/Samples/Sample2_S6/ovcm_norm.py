"""
 -------------------------------------------------------------
 Project:      I/O Data Normalization
 Version:      v.1.0
 Supervisor:   ENG. Michael B.Khani
 Developers:   Alperen Akgul, Esmaiel Abdi
 -------------------------------------------------------------
"""
import picamera
from PIL import Image

#Storing Data in a array
input_array =[0,0,0,0,0,0,0,0,0,0,0]

#Getting Data from a text file
sensor_data = open("sensor_data.txt", "r")

#Converting scene image to bitmap
camera = picamera.PiCamera()
image = camera.capture('scene.jpg')
image = image.tobitmap()
image.save('scene1.bmp')

#Gathering Data from text file
for i in range(11):
    input_array[i] = float(sensor_data.readline()[-10:])

#Data Normalization
for i in range(len(input_array)):
    if (type(input_array[i]) == int):
        input_array[i] = float(input_array[i])

    elif (type(input_array[i]) == bool):
        if (input_array[i] == True):
            input_array[i] = float(1)

        else: input_array[i] = float (0)

    elif (type(input_array[i]) == float):
        input_array[i] = float (input_array[i])

    else: input_array[i] == float (0)

print(input_array)