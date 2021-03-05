from PIL import Image
from cv2 import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=np.array(Image.open('image/timg.jpg').convert('L'))
image = mpimg.imread('image/timg.jpg')
rows,cols=img.shape
max=0
min=0
aver_sum=0
sum=0
k=0
for i in range(rows):
    for j in range(cols):
        if (max<img[i,j]):
            max=img[i,j]
for i in range(rows):
    for j in range(cols):
        if (min>img[i,j]):
            min=img[i,j]
for i in range(rows):
    for j in range(cols):
        sum+=img[i,j]
        k+=1
        aver_sum=sum/k
print('max:',max ,'min:' ,min, 'aver_sum:',aver_sum)
# plt.figure("lena")
# plt.imshow(img,cmap='gray')
# plt.axis('off')
# plt.show()
