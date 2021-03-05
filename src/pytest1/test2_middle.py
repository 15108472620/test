from PIL import Image
import numpy as np
from cv2 import cv2 as cv
def MidNoise(src,dst, probility = 0.05, method = "salt_pepper"):
 
	imarray = cv.imread(src)
	height, width = imarray[:,:,0].shape
 
	for i in range(height):
		for j in range(width):
			if np.random.random(1) < probility:
				if np.random.random(1) < 0.5:
					imarray[i, j] = 0
				else:
					imarray[i, j] = 255

	new_im = Image.fromarray(imarray)
	new_im.save(dst)
    
gray_girl = 'image/timg.jpg'
tar='image/middle.jpg'
MidNoise(gray_girl,tar)
img=cv.imread('image/middle.jpg')
cv.imshow('middle', img)
cv.waitKey()