import numpy as np
import cv2

image = cv2.imread("runway.jpg")

image = cv2.resize(image,(400,400)) 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)   
ret1,thresh = cv2.threshold(gray,230,255,cv2.THRESH_BINARY)  
blur =  cv2.GaussianBlur(thresh,(3,3),0)    #noise adjustment
k = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #contrast adjustment 
blur = k.apply(blur)

def autoCanny(blur, sigma=0.1):   #edge detection with canny algorithm
    median = np.median(blur)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(min(0,(1.0+sigma)*median))
    canny = cv2.Canny(blur,lower,upper)
    return canny

auto = autoCanny(blur)
    
cv2.imshow("RESULT",auto)

cv2.waitKey(0)
cv2.destroyAllWindows()