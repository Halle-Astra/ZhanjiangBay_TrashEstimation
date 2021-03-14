from ssea import *
from matplotlib import pyplot as plt 
from sklearn.cluster import AffinityPropagation

crossx_ls,crossy_ls = cross_esi('西北风')
train_set = np.c_[crossx_ls,crossy_ls]
train_set,_ = filt_points(train_set)
af = AffinityPropagation()
#af.fit(train_set)
#train_res = af.predict(train_set)

plt.plot(coast_x,coast)
#plt.plot(crossx_ls,crossy_ls,'r.')
plt.plot(train_set[:,0],train_set[:,1],'r.',alpha = 0.1)
plt.axis('equal')
plt.xlim(0,1000)
plt.show()
