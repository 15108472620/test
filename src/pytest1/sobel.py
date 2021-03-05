from cv2 import cv2 as cv
import numpy as np  
 
img = cv.imread("image/timg.jpg", 0)
 
x = cv.Sobel(img,cv.CV_16S,1,0)
y = cv.Sobel(img,cv.CV_16S,0,1)
 
absX = cv.convertScaleAbs(x)   # 转回uint8
absY = cv.convertScaleAbs(y)
 
dst = cv.addWeighted(absX,0.5,absY,0.5,0)
 
cv.imshow("absX", absX)
cv.imshow("absY", absY)
 
cv.imshow("Result", dst)
 
cv.waitKey(0)