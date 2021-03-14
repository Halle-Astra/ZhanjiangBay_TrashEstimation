# -*- coding: utf-8 -*-

import numpy as np 
from matplotlib import pyplot as plt 

def get_value(site,site1):
    return np.argmin(np.abs(site-site1))

damp = 1 

x = np.arange(1,10)
coast = np.sin(0.02*x)#定义海岸线离散点集
coast = np.sin(0.5*x)#定义海岸线离散点集
data_temp = np.load('xy.npz')
x,y = data_temp
x = data_temp[x]
coast = data_temp[y]
x = np.arange(10)
coast = np.sin(0.5*x)
#coast = x**2
tan = (coast[1:]-coast[:-1])/(x[1:]-x[:-1]+1e-16)#海岸线切线正切值（无问题）

#该如何定义水的流向
#若仅考虑较小的一段，考虑为单射函数，则
#后续版本可以考虑中心差分
vx = 0.5*x**2+1#避免第一个点是0，先如是考虑
vx = vx#构造x方向的水速
vy = vx**2#构造y方向的水速
#vy = -np.abs(vx)
#截取至方便计算
vx = vx[:-1]
vy = vy[:-1]

v = (vx**2+vy**2)**0.5#算出合速度大小
theta_w1 = np.arctan(vy/(vx+1e-16))#水与横轴的夹角
minus_pi_site = np.where((np.array(vx)<0) & (np.array(vy)<0))
theta_w1[minus_pi_site] -= np.pi
plus_pi_site = np.where((np.array(vx)<0) & (np.array(vy)>0))
theta_w1[plus_pi_site] += np.pi
    
theta_c = np.arctan(tan)#海岸线与横轴的夹角
theta_temp = 0.25*np.pi+theta_c-theta_w1#反射角#即使在sin与45°水流例子中依然成立（theta_c-theta_w)<0+0.5pi....result>0
#theta_w2 = theta_temp+theta_c-0.5*np.pi#反射角与横轴的夹角
#theta_w2 = np.abs(theta_temp)+np.abs(theta_c)-0.5*np.pi#这里得到的只能是正值，对于部分负值的情况，仍然需要寻找条件

theta_c = np.arctan(tan)
v1 = np.array((np.cos(theta_c),np.sin(theta_c))).T
v2 = np.array((np.cos(theta_c+0.5*np.pi),np.sin(theta_c+0.5*np.pi))).T
v3 = np.array((vx,vy)).T
theta_13 = []
for i in range(v3.shape[0]):
	theta_13_t = np.

v_2 = v*damp#damp为与河岸交换速度过程中的作用系数

crossx = np.zeros((theta_w2.size,theta_w2.size))
crossy = crossx.copy()
crossx_ls = []
crossy_ls = []
trash_m = []
for i in range(theta_w2.size):
    theta_1 = theta_w2[i]
    for j in range(i+1,theta_w2.size):
        theta_2 = theta_w2[j]
        #x3 = (x[i]*np.tan(theta_1)-x[j]*np.tan(theta_2))/(np.tan(theta_1)-np.tan(theta_2))
        x3 = (coast[i]-coast[j]-np.tan(theta_1)*x[i]+np.tan(theta_2)*x[j])/(np.tan(theta_2)-np.tan(theta_1))
        y3 = coast[j]+(x3-x[j])*np.tan(theta_2)#到这一步得到了交点公式
        crossx[i][j] = x3 
        crossy[i][j] = y3 
        vec_x3 = np.array((x3,y3))
        vec_x2 = np.array((x[j],coast[j]))
        vec_x32 = vec_x2-vec_x3
        if np.dot(vec_x32,np.array((np.cos(theta_w2[j]),np.sin(theta_w2[j]))))>0:
            continue
        trash_m.append(v[i]+v[j])#水的输送量，但是水速越快，垃圾越不容易留下来
        crossx_ls.append(x3)
        crossy_ls.append(y3)
#这套算法似乎没有明显错误
#没办法，考虑旧的水流的话能裂开，没法构建出合理的模型，或者说damp取值为多少没法得到
#而且很容易把考虑的计算的点扩展到整个二维平面上

###########################################
#计算反射线（确为反射线的前提：反射线的过滤条件无误
#考虑计算切线，对于给定x_0,y_0,有(y-y_0)/(x-x_0)=tan(theta)
# ====> y=tan(theta)(x-x_0)+y_0
#红色的球是交点
plt.plot(x,coast)
plt.plot(crossx_ls,crossy_ls,'r.')#,alpha = 0.5);#plt.xlim(0,300);plt.ylim(0,100)#plt.xlim(0,300);plt.ylim(0,100)
# =============================================================================
# for i in range(len(x)):#range(10,250,20):
#     for j in range(i,len(x)-1):#range(i,250,20):
#         fig = plt.figure(figsize = (15,5))
#         ax = fig.add_subplot(131)
#         plt.plot(x,coast)
#         plt.plot(x[i],coast[i],'bo',markersize = 10)
#         plt.plot(x[j],coast[j],'go',markersize = 10)
#         plt.plot(crossx[i][j],crossy[i][j],'ro',markersize = 10)
#         plt.axis('equal')
#         plt.axis('equal')
#         ax = fig.add_subplot(132)
#         ax.plot(x,coast)
#         ax.plot([x[i],crossx[i][j]],[coast[i],crossy[i][j]],'b',markersize = 10);plt.xlim(x[i]-3,x[i]+3);plt.ylim(coast[i]-1,coast[i]+1)
#         plt.plot(crossx[i][j],crossy[i][j],'ro',markersize = 10)
#         #计算切线
#         x_tan = np.arange(x[i]-3,x[i]+4)
#         y_tan = tan[i]*(x_tan-x[i])+coast[i]
#         plt.plot(x_tan,y_tan,'--')
#         ax.axis('equal')
#         ax = fig.add_subplot(133)
#         plt.plot(x,coast)
#         plt.plot([x[j],crossx[i][j]],[coast[j],crossy[i][j]],'g',markersize = 10);plt.xlim(x[j]-3,x[j]+3);plt.ylim(coast[j]-1,coast[j]+1)
#         plt.plot(crossx[i][j],crossy[i][j],'ro',markersize = 10)
#         #计算切线
#         x_tan = np.arange(x[j]-3,x[j]+4)
#         y_tan = tan[j]*(x_tan-x[j])+coast[j]
#         plt.plot(x_tan,y_tan,'--')
#         ax.axis('equal')
#         plt.pause(0.5)
# plt.show()
# =============================================================================
# =============================================================================
# 好象不如直接拿去给matlab做线性插值
# #绘制浓度分布，相当于提供了一个权重
# a = np.arange(min(crossx_ls),max(crossx_ls)+1)#对应于x轴
# b = np.arange(min(crossy_ls),max(crossy_ls)+1)#对应于y轴
# A,B = np.meshgrid(a,b)
# M = np.zeros(A.shape)
# for i in range(len(trash_m)):
#     M[b==crossy_ls[get_value(b[i],crossy_ls)],a==crossx_ls[i]]=trash_m[i]
# plt.contourf(A,B,M)
# =============================================================================
plt.show()