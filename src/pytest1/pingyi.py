from cv2 import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
def fft2_log(data):
    res = np.fft.fft2(data)
    res = np.log(np.abs(res) + (1 ** -10))
    res = np.fft.fftshift(res)
    return res

def show_imgs(imgs, titles):
    fig, axs = plt.subplots(nrows = 1,ncols = len(imgs), figsize = [20,20])
    for i in range(len(imgs)):
        axs[i].imshow(imgs[i],cmap = plt.get_cmap('gray'))
        axs[i].set_xlabel(titles[i])
    return fig

# 平移
I = Image.open('image/qq.jpg').convert('L')
I = np.array(I)
img = np.pad(I, ((0,512),(0,512)))
img_fft = fft2_log(img)
res = np.pad(I, ((512,0),(0,512)))
res_fft = fft2_log(res)

show_imgs([img,img_fft, res,res_fft],['img','img_fft','move','move_fft'])

# 旋转
I = Image.open('lena.png').convert('L')
img = np.array(I)
img = np.pad(I, ((256,256),(256,256)))
img_fft = fft2_log(img)

res = Image.fromarray(img).rotate(45)

res = np.array(res)
res_fft = fft2_log(res)

show_imgs([img,img_fft, res,res_fft],['img','img_fft','rotate','rotate_fft'])

