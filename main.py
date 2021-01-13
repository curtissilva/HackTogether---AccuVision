import cv2 as cv
import numpy as np

video = cv.VideoCapture('City.mp4')
ret, frame1 = video.read()
ret, frame2 = video.read()


while video.isOpened():
    difference = cv.absdiff(frame1, frame2)
    greyScale = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(greyScale, (5,5), 0)
    _, thresh = cv.threshold(blurred, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame1, contours, -1, (0,255,0), 2)

    cv.imshow("TEST", frame1)
    frame1 = frame2
    ret, frame2 = video.read()

    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
video.release()