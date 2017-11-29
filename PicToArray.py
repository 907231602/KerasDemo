#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#把图片转换成黑白图片，然后转换成数组
#参考：http://blog.csdn.net/lql0716/article/details/52416086
from PIL import Image
import numpy as np
import os
# import scipy
import matplotlib.pyplot as plt
from GetPicInfo import *
from pylab import *


#把彩色图片变灰，然后分解成数组  [ 0.73333333,  0.73333333,  0.73333333, ...,  0.73333333, 0.73333333,  0.73333333],
def ImageToMatrix(filename):
    # 读取图片
    im = Image.open(filename)
    #print(im)
    # 显示图片
#     im.show()
    width,height = im.size
    im = im.convert("L")
    data = im.getdata()
    data = np.matrix(data,dtype='float')/255.0
    #new_data = np.reshape(data,(width,height))
    new_data = np.reshape(data,(height,width))
    return new_data
#     new_im = Image.fromarray(new_data)
#     # 显示图片
#     new_im.show()

#把图片对应的数组转化成图片（黑白）
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im

#通过循环，把路径下图片转换成数组
def getPicArray(filePath):
    #path='D:\AI\pythonPack\pic120_30\\'
    myfile= MyFileInfo()
    total=myfile.totalfile(filePath)
    print('total',total)
    fileName=myfile.getFilesName();
    area=np.zeros(shape=(total,30,120))
    #print(area)
    i=0
    for name in fileName:
        area[i]= ColorToBlackArray(filePath+name)
        i=i+1
    #print('area',area)
    #print(fileName)
    return area,fileName


#读取图片, 灰度化，并转为数组 [221 221 221 ....221 221 221 221 221 221 221 221]
def ColorToBlackArray(path):
    im = array(Image.open(path).convert('L'))
    im2=255-im  # 对图像进行反相处理,白色的为0，黑色为255
    #print(type(im2))
    return im


if __name__ == "__main__":
    getPicArray('D:\AI\pythonPack\pic120_30_test\\')

    # filename = r'pic\login.png'
    # data = ImageToMatrix(filename)
    # print(data)

    #new_im = MatrixToImage(data)
    #plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
    #new_im.show()
    #new_im.save('lena_1.bmp')