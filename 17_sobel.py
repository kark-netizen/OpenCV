import cv2 as cv
import numpy as np
import sys 

src=cv.imread('cake_1.jpg')
gausblur=cv.GaussianBlur(src,(3,3),0)
gray=cv.cvtColor(gausblur,cv.COLOR_BGR2GRAY)
grad_x=cv.Sobel(gray,1,0,3)
grad_y=cv.Sobel(gray,0,1,3)

abs_grad_x=cv.convertScaleAbs(grad_x)
abs_grad_y=cv.convertScaleAbs(grad_y)

grad=cv.addWeighted(abs_grad_x)

