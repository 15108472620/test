from cv2 import cv2 as cv
import numpy as np  
 
img = cv.imread("image/timg.jpg", 0)
 
gray_lap = cv.Laplacian(img,cv.CV_16S,ksize = 3)
dst = cv.convertScaleAbs(gray_lap)
 
cv.imshow('laplacian',dst)
cv.waitKey(0)
cv.destroyAllWindows()