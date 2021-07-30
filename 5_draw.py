import numpy as np
import cv2 as cv

img=cv.imread('cake_1.jpg', cv.IMREAD_COLOR)
def rescaleFrame(frame):
    dimensions=(1920, 1080)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img=rescaleFrame(img)

cv.line(img, (0,0), (140,140), (255,0,0,), 15)
#draw line (on image, starting from (0,0), ending at (140,140), colour (b,g,r), 15 pixels) 

cv.rectangle(img, (10,10), (80, 100), (255, 255, 0), 10)
#draw a rectangle

cv.circle(img, (100,200), 58, (0,0,255), -1)
#draw a circle. -1 indicates fill inside

pts=np.array([[10,5],[220,300],[350,700],[400,630],[450,221],[90,901]],np.int32)
cv.polylines(img, [pts], True, (0,255,0), 5)

cv.imshow('Cake',img)
cv.waitKey(0)
cv.destroyAllWindows()

