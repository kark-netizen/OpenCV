import cv2 as cv
import numpy as np

img=cv.imread('cake_1.jpg')
cv.imshow('Cake', img)

cv.waitKey(5000)
#5000ms

#to scale the above image

def rescaleFrame(frame, scale=0.5):
    #set scale to a suitable value
    #works for images, videos and live videos

    width= int(frame.shape[1]*scale)
    #frame.shape[1] returns width of frame
    height=int(frame.shape[0]*scale)
    #frame.shape[0] retruns height of frame
    dimensions=(width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img=rescaleFrame(img)
cv.imshow('Rescaled Cake', img)
cv.waitKey(5000)

cv.destroyAllWindows()

def rescaleResolution(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)


capture=cv.VideoCapture(0)
while True:
    isTrue, frame=capture.read()

    cv.imshow('Your face', frame)#display frame

    if cv.waitKey(20) & 0xFF==ord(' '):#' ' is used to end video
        break
capture.release()
cv.destroyAllWindows()

def rescaleResolution(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

 



