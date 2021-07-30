import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

while True:
    isTrue, frame=cap.read()

    laplacian=cv.Laplacian(frame, cv.CV_64F)
    #CV_64F is a data type
    cv.imshow('original', frame)
    cv.imshow('laplacian', laplacian)

    if cv.waitKey(1) & 0xFF==ord(' '):
        break

cap.release()
cv.destroyAllWindows()



