import numpy as  np
import cv2 as cv

img=cv.imread('cake_1.jpg', cv.IMREAD_COLOR)

#adding fonts
font=cv.FONT_HERSHEY_COMPLEX
cv.putText(img, 'This Cake', (0,130), font,1,(200,220,200), 2, cv.LINE_AA)

cv.imshow('Cake', img)
cv.waitKey(5000)
cv.destroyAllWindows()
