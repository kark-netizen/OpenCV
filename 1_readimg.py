import cv2 as cv

#reading videos
img=cv.imread('celebs.jpg')
#mentioning path is required if image is outside of working dir
cv.imshow('Cake',img)

cv.waitKey(0)
#waits in ms for a key to be pressed
   

#reading videos
#capture=cv.VideoCapture(0)
#to read videos from your web cam
#0 is used to reference the webcam


