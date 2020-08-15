import cv2
import numpy as np

img = cv2.imread("path")
#To get the size of image
print(img.shape)
#Resize the image
#Width ....Height
imageResize = cv2.resize(img,(300,200))

#Image cropping
#Height ....Width
#Starting point:Ending point
imgCropped = img[0:200,200:500]


cv2.imshow("Lambo",img)
cv2.imshow("Resized Image",imageResize)
cv2.imshow("Cropping Image",imgCropped)


cv2.waitkey(0)