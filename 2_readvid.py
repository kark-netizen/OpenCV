import cv2 as cv

#reading videos

capture=cv.VideoCapture(0)
#to read videos from your web cam
#0 is used to reference the webcam

#capture=cv.VideoCapture('cake_2.mp4')

#to read video frame by frame 
while True:
    isTrue, frame=capture.read()

    cv.imshow('Cake_Video', frame)#display frame

    if cv.waitKey(20) & 0xFF==ord(' '):#' ' is used to end video
        break
capture.release()
cv.destroyAllWindows()
