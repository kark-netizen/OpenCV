import numpy as np
import cv2 as cv

img1=cv.imread('img_3.jpeg')
img1gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
_,img1cvt=cv.threshold(img1gray,100,255,cv.THRESH_BINARY)


cv.imshow('img1',img1)
cv.imshow('img1gray',img1gray)
cv.imshow('img1cvt',img1cvt)
cv.waitKey(0)
cv.destroyAllWindows()