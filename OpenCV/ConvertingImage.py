import cv


#To read the image
img = cv2.imread("path")


#To convert the image to grey
imgGray = cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)

#To convert into blur//Blur value (must be odd numbers)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gray Image",imgBlur)
#To Convert to canny //threshold value
imgCanny = cv.Canny(img,100,100)
cv2.imshow("Canny Image",imgCanny)

#To enhance the canny image by dilation method
#Dilation makes the image tick and one can tell the difference in color
#Eroded makes the imgae thin


import  numpy as np
kernel = np.ones(5,5),np.uint8)
imgDialation = cv2.dilate(imgCanny,kernel,iteration = 1);
cv2.imshow("Dilated  Image",imgDialation);


#Erosion
imgEroded = cv2.erode(imgDialation,kernel,iteration = 1);
cv2.imshow("Eroded Image",imgDialation);








#To set the time
cv.wait(0)