import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

lena = mpimg.imread('image/timg.jpg') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
lena.shape #(512, 512, 3)

#显示图片
# plt.imshow(lena) # 显示图片
# plt.axis('off') # 不显示坐标轴
# plt.show()

#灰度图
# def rgb2gray(rgb):
#     return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
# gray = rgb2gray(lena)    
# plt.imshow(gray, cmap = plt.get_cmap('gray'))
# # plt.imshow(gray, cmap='Greys_r')plt.axis('off')
# plt.show()

#拉伸图片
from scipy import misc
lena_new_sz = misc.imresize(lena, 0.5) # 第二个参数如果是整数，则为百分比，如果是tuple，则为输出图像的尺寸
plt.imshow(lena_new_sz)
plt.axis('off')
plt.show()