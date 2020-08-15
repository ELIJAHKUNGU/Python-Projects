import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#To color the image
#img[:] = 255,0,0
#Adding a line
#Starting point ,The Ending point,Color and Thickness
cv2.line(img,(0,0),(300,300),(0,255,0),3)

#The whole image
#Width and Height
#cv2.line(img,(0,0),(img.shape[1],img.shape[0],(0,255,0),3)

#Adding a Rectangle
#Starting point ,The Ending point,Color and Thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#To fill the whole Rectangle section
#cv2.line(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

#Adding a Circle
#Starting point ,The radius,Color and Thickness
cv2.circle(img,(0,0),(250,350),(0,0,255),5)


#Adding a Text
#The text,Starting point ,Font,Scale,Color and Thickness
cv2.putText(img,"Hello world",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)


cv2.imshow("Image",img)
cv2.waitkey(0)
