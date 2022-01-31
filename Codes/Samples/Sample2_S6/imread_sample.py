
#LIBRARIES
import numpy as np

# image read libraries
from PIL import Image
import cv2
import matplotlib.pyplot as plt 
import skimage
from skimage import io

#IMAGE NAME TO LOAD
img_dir = 'scene.jpg'

#IMPLEMENTATION
# matplotlib
print('plt.imread()')
img1 = plt.imread(img_dir)
print(type(img1))#np.array
print(img1.shape)
print('\n')

# opencv 
print('cv2.imread()')
img2=cv2.imread(img_dir)
print(type(img2))
print(img2.shape)
print('\n')

# PIL
print('Image.open()')
img3=Image.open(img_dir)
print(type(img3)) # PIL.JpegImagePlugin.JpegImageFile object
img3=np.array(img3)# convert to np array
print(type(img3))
print(img3.shape)
print('\n')

# skimge 
print('io.imread()')
img4 = io.imread(img_dir)
print(type(img4))#np.array
print(img4.shape)