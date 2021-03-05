from cv2 import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
# 绘制图像灰度直方图
def deaw_gray_hist(gray_img):
    '''
    :param  gray_img大小为[h, w]灰度图像
    '''
    # 获取图像大小
    h, w = gray_img.shape
    gray_hist = np.zeros([256])
    for i in range(h):
        for j in range(w):
            gray_hist[gray_img[i][j]] += 1
    x = np.arange(256)
    # 绘制灰度直方图
    plt.bar(x, gray_hist)
    plt.xlabel("gray Label")
    plt.ylabel("number of pixels")
    plt.show()
    return 0

# 读取图片
img = cv.imread('image/timg.jpg') # 这里需要指定一个 img_path
deaw_gray_hist(img[:,:,0])
cv.imshow('ori_img', img)
cv.waitKey()

# 灰度图
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
gray = rgb2gray(img)    
plt.imshow(gray, cmap = plt.get_cmap('gray'))
# plt.imshow(gray, cmap='Greys_r')plt.axis('off')
plt.show()

# 反转变换
reverse_img = 255 - img
cv.imshow('srcimg',img)
cv.imshow('reverse_img',reverse_img)
cv.waitKey(0)

# 对数变换
def logTransform(c,img):

    #3通道RGB
    '''h,w,d = img.shape[0],img.shape[1],img.shape[2]
    new_img = np.zeros((h,w,d))
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i,j,k] = c*(math.log(1.0+img[i,j,k]))'''

    #灰度图专属
    h,w = img.shape[0], img.shape[1]
    new_img = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * (math.log(1.0 + img[i, j]))
    new_img = cv.normalize(new_img,new_img,0,255,cv.NORM_MINMAX)
    return new_img
log_img = logTransform(3.0,img)
cv.imshow('log_img',log_img)
cv.waitKey(0)

# 指数变换
def gammaTranform(c,gamma,image):
    h,w,d = image.shape[0],image.shape[1],image.shape[2]
    new_img = np.zeros((h,w,d),dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i,j,0] = c*math.pow(image[i, j, 0], gamma)
            new_img[i,j,1] = c*math.pow(image[i, j, 1], gamma)
            new_img[i,j,2] = c*math.pow(image[i, j, 2], gamma)
    cv.normalize(new_img,new_img,0,255,cv.NORM_MINMAX)
    new_img = cv.convertScaleAbs(new_img)

    return new_img
new_img = gammaTranform(1,2.5,img)
cv.imwrite(r'image/new_img.jpg',new_img)
cv.imshow('x',new_img)
cv.waitKey(0)


# def ExpTran(src, esp = 0, gama = 1):
# 	im = Image.open(src)
# 	imarray = np.array(im)
# 	height, width = imarray.shape
 
# 	for i in range(height):
# 		for j in range(width):
# 			tmp = imarray[i, j]/255
# 			tmp = int(pow(tmp + esp, gama)*255)
# 			if tmp >=0 and tmp <= 255:
# 				imarray[i, j] = tmp
# 			elif tmp > 255:
# 				imarray[i, j] = 255
# 			else:
# 				imarray[i, j] = 0
# 	plt.imshow(imarray, cmap = plt.get_cmap('zhishu'))
#     # plt.imshow(gray, cmap='Greys_r')plt.axis('off')
#     plt.show()
# 	print("Suceessfully transform!")
 
# ExpTran('image/timg.jpg', 0, 5)


# 锐化空间滤波器
def Sharp(img,flag1=0,flag2=0):
    w = img.width
    h = img.height
    size = (w,h)
    iSharp = cv.CreateImage(size,8,1)
    for i in range(h-1):
        for j in range(w-1):
            if flag2 == 0:
                x = abs(img[i,j+1]-img[i,j])
                y = abs(img[i+1,j]-img[i,j])
            else:
                x = abs(img[i+1,j+1]-img[i,j])
                y = abs(img[i+1,j]-img[i,j+1])
            if flag1 == 0:
                iSharp[i,j] = max(x,y)
            else:
                iSharp[i,j] = x+y
    return iSharp 
iMaxSharp = Sharp(img)
iAddSharp = Sharp(img,1)
iRMaxSharp = Sharp(img,0,1)
iRAddSharp = Sharp(img,1,1)
cv.ShowImage('iMaxSharp',iMaxSharp)
cv.ShowImage('image',img)
cv.ShowImage('iAddSharp',iAddSharp)
cv.ShowImage('iRAddSharp',iRAddSharp)
cv.ShowImage('iRMaxSharp',iRMaxSharp)
cv.WaitKey(0)

# 平滑空间滤波器
def wgn(x,snr):
    snr = 10 ** (snr / 10.0)
    xpower = np.sum(x ** 2) / len(x)
    npower = xpower / snr
    return np.random.randn(len(x)) * np.sqrt(npower)
rows, cols = img.shape 
original_noise = img.copy().astype(np.float64)
for i in range(cols):
    original_noise[:, i] += wgn(original_noise[:, i], 10)
plt.imshow(original_noise, "original_noise", 2, 2, 2)