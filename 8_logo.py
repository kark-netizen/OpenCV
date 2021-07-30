import numpy as np
import cv2 as cv

logo=cv.imread("Task/agent_p_logo.png")
img=cv.imread("Task/celebs.jpg")

#graying
logoGray=cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
#thresholding 
thres=220
thres,mask1=cv.threshold(logoGray,thres,255,cv.THRESH_BINARY_INV)
#threshold returns two outputs, threshold and image
#anything below threshold =0, anything above threshold=1, cv.thresh_binary_inv is used to inverse this
#cv.threshold accepts binary image

#area selection
rows, cols, ses= logo.shape
roi=img[0:rows,0:cols]

#bitise operation to mask the image
maskInv=cv.bitwise_not(mask1)

#crop logo
#choose the values of the background where mask is set to 1
img_bg=cv.bitwise_and(roi,roi,mask=maskInv)
#chllse the values of logo where mask is set to 1
img_fg=cv.bitwise_and(logo, logo, mask=mask1)

#create final image
dst=cv.add(img_bg,img_fg)
img[0:rows,0:cols]=dst

cv.imshow('logoInv',maskInv)
cv.imshow('mask',mask1)
cv.imshow('bg',img_bg)
cv.imshow('fg',img_fg)
cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()