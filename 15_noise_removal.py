import cv2 as cv
import numpy as np

#https://docs.opencv.org/4.5.2/d4/d13/tutorial_py_filtering.html

xvid=cv.VideoCapture(0)

while True:
    isTrue, frame=xvid.read()
    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
    lowerlimit=np.array([10,100,120])
    upperlimit=np.array([30,255,255])

    mask=cv.inRange(hsv,lowerlimit,upperlimit)
    res= cv.bitwise_and(frame,frame,mask=mask)

    #averaging
    kernel=np.ones((15,15),np.float32)/225
    #create a 15x15 matrix. every pixel in new image
    #of this matrix
    #will have 1/(15*15) contribution from the neighbours
    smoothed=cv.filter2D(res,-1,kernel)

    #gausian blur
    gaussblur=cv.GaussianBlur(res,(15,15),0)

    #median blur
    medianblur=cv.medianBlur(res,15)

    cv.imshow('Captured Video ', frame)
    cv.imshow('mask  ', mask)
    cv.imshow('res ', res)
    cv.imshow('smoothed', smoothed)
    cv.imshow('gaussblur', gaussblur)
    cv.imshow('medianblur  ', medianblur)

    if cv.waitKey(1) & 0xFF==ord(' '):
        break

xvid.release()
cv.destroyAllWindows() 

