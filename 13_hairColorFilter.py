import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.9):
    width= int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img=cv.imread('image.png')
img=rescaleFrame(img)

#convert to hsv(hue saturation value)
imgHsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
solidcolor=np.zeros((img.shape[0],img.shape[1],3),np.uint8)
solidcolor[:]=(255, 153, 255)



#range creation [hue,sat,value]
lowercolor=np.array([100,0,0])
uppercolor=np.array([140,255,255])
canny=cv.Canny(img,0,0)
mask=cv.inRange(imgHsv,lowercolor,uppercolor)
mask1=cv.bitwise_and(canny,mask,mask=mask)
maskinv=cv.bitwise_not(mask)


cv.imshow('mask',mask)
cv.imshow('mask1',mask)
"""

cv.imshow('maskinv',maskinv)
cv.imshow('solidcolor',solidcolor)
cv.imshow('canny',canny)"""
cv.waitKey(0)
cv.destroyAllWindows()
