import cv2 as cv

im = cv.imread('leaf.JPG')
cv.imshow('result',im)
cv.waitKey(0)
cv.destroyAllWindows()
