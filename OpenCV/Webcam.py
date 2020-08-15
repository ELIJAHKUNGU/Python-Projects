import cv2

#Index of the camera
cap = cv2.VideoCapture(0)

#Width
cap.set(3,640)
#Height
cap.set(4,480)
#Brightness
cap.set(10,100)
while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break