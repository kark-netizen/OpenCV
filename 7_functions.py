import numpy as np
import cv2 as cv


img=cv.imread('task/agent_p_logo.png')

#graying
grayImg=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",grayImg)

# blur(gaussian)
blurImg=cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
#kernel size has to be odd number. increase it for increased blur
cv.imshow("Blur", blurImg)

#edge cascade
cannyImg= cv.Canny(img, 125, 175)
cv.imshow("Canny", cannyImg)

cv.waitKey(0)
