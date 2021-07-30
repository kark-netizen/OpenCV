import cv2 as cv
import numpy as np

capture=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')
#no idea what this is. used to save output video
out=cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))
#saving output


while True:
    isTrue, frame=capture.read()
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    out.write(frame)
    #creating output 

    cv.imshow('Your Face', frame)#display frame
    cv.imshow('Your Face in gray', gray)
    if cv.waitKey(1) & 0xFF==ord(' '):#' ' is used to end video
        break

capture.release()
out.release()
cv.destroyAllWindows()