import numpy as np
from PIL import Image
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from tkinter import filedialog
def filterImage(srcImage,max):
    #打开图像文件并获取数据
    srcIm = Image.open(srcImage).convert('L')
    fd_Im=fft2(srcIm)
    fd_Im=fftshift(fd_Im+10)#移动一下
    #虚部i
    imag_Data=np.abs(np.imag(fd_Im))
    outData1=imag_Data/max
    outIm1 = Image.fromarray(outData1)
    outIm1.show()
    #实部
    real_Data = np.abs(np.real(fd_Im))
    outData2 = real_Data /max
    outIm2 = Image.fromarray(outData2)
    outIm2.show()
    #绝对值
    abs_Data = np.abs(fd_Im)
    outData3 = abs_Data /max
    outIm3 = Image.fromarray(outData3)
    outIm3.show("频率")
    #返回原图
    fd_Im = ifftshift(fd_Im)
    temp=ifft2(fd_Im)
    outData=np.uint8(np.real(temp))
    outIm=Image.fromarray(outData)
    outIm.show("时间")

filterImage('image/timg.jpg',3)