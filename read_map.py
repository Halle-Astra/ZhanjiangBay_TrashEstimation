# -*- coding: utf-8 -*-

from scipy.io import loadmat
from matplotlib import pyplot as plt 
import cv2 
import numpy as np 
import pywt 

def wv_rn(data):
    if len(data.shape)==2:
        data = data.tolist()[0]
    elif len(data.shape)==1:
        data = data.tolist()
    index = len(data)
    # Create wavelet object and define parameters
    w = pywt.Wavelet('db8')  # 选用Daubechies8小波
    maxlev = pywt.dwt_max_level(len(data), w.dec_len)
    #print("maximum level is " + str(maxlev))
    threshold = 0.1
    # Threshold for filtering

    # Decompose into wavelet components, to the level selected:
    coeffs = pywt.wavedec(data, 'db8', level=maxlev)  # 将信号进行小波分解
    for i in range(1, len(coeffs)):  
        coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))  # 将噪声滤波
    datarec = pywt.waverec(coeffs, 'db8')  # 将信号进行小波重构
    return datarec

def em_rn(data):
	for i in range(len(data)):
		if i-1<0:
			continue
		if i+1>len(data)-1:
			continue
		data[i]=0.25*data[i-1]+0.5*data[i]+0.25*data[i+1]
	return data

data = loadmat('map_zj.mat')['i4']
plt.figure()
plt.imshow(data)
data_t = data[606:800,450:700]
plt.figure()
plt.imshow(data_t)
site = np.where(data_t!=0)
print(site)
x = list(set(site[1]))
y = [max(site[0])-max(site[0][site[1]==i])   for i in x]
y = np.array(y)
x = np.array(x)
plt.figure()
plt.plot(x,y)

y = em_rn(wv_rn(y))
plt.figure()
plt.plot(x,y)
plt.show()

np.savez('xy',x,y)
'''
data = cv2.Canny(data,0,1)
plt.figure()
plt.imshow(data)
'''