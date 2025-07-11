
# MOVING OBJECT DETECTION - @suraj_nate

import cv2 #opencv
import time #delay
import imutils #resize

cam = cv2.VideoCapture(0) #cam id - 0, 1, 2, 3
time.sleep(1)

firstFrame = None
area = 500

while True:
    _, img = cam.read() # read from the camera ret,img(_) - basically a placeholder
    text = "Normal"

    img = imutils.resize(img,width=800) #resize

    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #color 2 gray scale image

    gaussianimg = cv2.GaussianBlur(grayimg,(21,21),0) #Smoothened

    if firstFrame is None:
        firstFrame =  gaussianimg #capturing the first frame
        continue

    imgDiff = cv2.absdiff(firstFrame,gaussianimg) #abs-absolute diff-difference

    threshimg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]

    threshimg = cv2.dilate(threshimg,None, iterations=2) #left overs-erotion or dilation

    cnts = cv2.findContours(threshimg.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # make complete Contours

    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area : #make full area
            continue

        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
        text = "Moving Object Detected Successfully"

    cv2.putText(img,text,(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Camera Feed", img)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
