import cv2 as cv
import numpy as np

#thresholding to simplify lowlight images

img=cv.imread('bookpage.jpg')

#bgrtogray
img2Gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#threshold
thresh,imgthresh=cv.threshold(img,10,255,cv.THRESH_BINARY)
thresh,imgGraythresh=cv.threshold(img2Gray,10,255,cv.THRESH_BINARY)

#adaptive threshold
imgadaptive=cv.adaptiveThreshold(img2Gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
#accepts grayscaled image
imgadaptive2=cv.adaptiveThreshold(img2Gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,115,1) 

cv.imshow('img',img)
cv.imshow('thresh',imgthresh)
cv.imshow('imgGray',img2Gray)
cv.imshow('imgGraythresh',imgGraythresh)
cv.imshow('imgadaptive',imgadaptive)
cv.imshow('imgadaptive2',imgadaptive2)
cv.waitKey(0)
cv.destroyAllWindows()
