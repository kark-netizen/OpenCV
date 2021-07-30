import cv2 as cv

img1=cv.imread('perry_1')
img2=cv.imread('perry_2')



cv.imshow('img1',img1)
cv.imshow('img2',img2)

cv.waitKey(0)
cv.destroyAllWindows()