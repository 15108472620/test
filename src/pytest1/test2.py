import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
from PIL import Image
import numpy as np

img = mpimg.imread('image/timg.jpg') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
image=Image.open('image/timg.jpg')
rows,cols = img[:,:,0].shape
f = open("o.txt", 'w+')  
rgb_im = image.convert('RGB')

r, g, b = rgb_im.getpixel((2, 2))
print(r, g, b,file=f)
print (111)
# for i in range(0,rows):
# 	for j in range(0,cols):
# 		r, g, b = rgb_im.getpixel((i, j))
# 		print(r, g, b,file=f)
im=np.asarray(img)
max=0
min=im[0]
aver_sum=0
k=0
for i in range(1,len(im)):
    if  max<im[i]:
        max=im[i]
for y in im:
    if min>y:
        min=y
for x in im:
    sum+=x
    k+=1
    aver_sum=sum/k
print ('最大值等于 %d' % (max))
print ('最小值等于 %d' % min)
print ('均值等于 %d' % aver_sum)