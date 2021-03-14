# -*- coding: utf-8 -*-
import numpy as np 
from matplotlib import pyplot as plt 

coast_txt = '70.38404228477067	70.7377611871728	71.32808403652885	71.92542684141185	72.43099813907867	72.96869540983428	73.3793987506353	73.81192013616146	74.32262280726555	74.72937227677205	75.08066243770631	75.15397177009316	75.53011168151919	76.35030999779465	76.76246377524616	77.36355663295681	77.80697908530104	78.38205850985814	79.09411804409736	79.6973061733228	80.15458096023976	80.74112089061165	81.28327385947648	81.70438530404381	82.27054465330004	82.6466119980671	83.08766874448281	83.58844182040787	83.89039209518833	84.16744909425032	84.37200712647908	84.65991516037518	85.01657363559819	85.29093762529308	85.50255936850775	85.82651139553067	86.32129142369452	86.9178075729872	87.44985514390359	87.68827993977864	87.50944877597189	86.85660089538312	86.02312693533503	85.45620876716893	85.18378096491047	84.76964535297101	84.22365944088735	83.92894360096358	83.66721946723473	83.13907427085121	82.64981371486574	81.9404809877423	80.71861318538976	78.93923643649502	77.39444495574747	75.65531753958001	74.3326764061046	73.41608739730432	72.3571507603265	70.63490444533123	68.46765618906382	67.03766288189601	65.749604737688	62.21453334766436	54.72598465745872	47.41922489341726	44.657566200963586	43.07888952723648	40.75756525322306	38.648600402789	36.12681357901546	34.02368728092076	32.572885322613956	31.20502950564515	29.716036692713704	28.397742470504355	27.10811321739297	25.637146132584554	23.8552988054435	21.664833441206305	19.304536324804786	17.3305825899181	15.924253062349187	14.796313905087509	13.752614997047605	12.717955969028203	11.763838371520052	10.986199423823084	10.144051467053995	9.498045898631984	9.174501353960842	8.876558925266258	8.668029618036973	8.430552097442087	7.894684101440229	6.927507951036395	5.921496617443683	5.242957105134755	4.470518656244107	3.8938951672206032	3.1696515956951474	2.3507061646098317	1.547042568272398	1.0160962004570568	0.7881352326324903	0.6003043482870623	0.3648097250536013	0.17259603625035566	0.04495718065465587	9.030771920836081e-05	0.02960643813863448	0.035692173713357686	-0.011860125430807352	-0.054948346334293754	-0.07376403964806516	-0.05175412733404933	0.11795248314609516	0.5371045981319293	1.0159611566880025	1.2579563250125223	1.379695348375987	1.589623178351121	2.017580203325206	2.405471812761733	2.611761256809988	2.8298286321454005	3.0103609663882795	3.1426103397983187	3.2401540606590347	3.293570218456984	3.301726382034415	3.2865746036953807	3.2648591379194083	3.249066590415582	3.2459909185143263	3.2543533502634494	3.293412853757097	3.3900857132373954	3.49547440703077	3.529746172601694	3.622854845792967	3.8618139183563507	3.9536789760133746	4.0313185892806365	4.212578731341088	4.310618719719117	4.417329106393094	4.515260422603292	4.61118564585243	4.714054468578936	4.827455810016113	4.946616685911019	5.059863595381696	5.150596601155944	5.210065549855707	5.243150575236788	5.258269755722903	5.265212707232154	5.268204946494954	5.259349613201016	5.229346198756556	5.17118622383863	5.0838557203962935	4.978333936931056	4.8694580917182	4.766211768662836	4.650711213634316	4.482406571833632	4.273484685330637	4.09516738673907	3.960168178916943	3.8315637896337558	3.7218010901347625	3.6760706901077853	3.6960865019605693	3.7577737719179254	3.8665537519211344	4.038078606864209	4.234657898082548	4.423254326215453	4.793185258302106	5.40440121573615	6.067153881328951	7.006337661057961	7.833946482364835	8.792783318341707	9.620243786035882	10.380051184540983	11.33881213503209	11.73913629401915	11.733141192442499	11.61530040058059	11.619365692453778	11.883050476915109	12.484005214765544	13.122592642097201	13.468171604154985	13.777043862750505	13.85362199494957	13.644655518304688	16.66707780910795	23.75056847847022	25.435906828290445	25.998505876031206	26.169781613861122	26.48902950455903	27.328807694148278	27.805256317100536	27.917058097965203	27.977051808755323	28.19705290184548	28.312196128851127	28.513323681574043	28.99311317304667	29.556693268097902	30.43393459700344	32.31657394133081	34.55704958412306	37.040746482935035	38.24167950622797	38.42831644460377	38.572110116539896	38.988788846575744	39.41290827018334	39.6413638295544	39.75634330151359	39.834941340086786	40.30627003193701	41.12662692259052	41.72371314445744	41.94029601531473	42.034528232968704	42.161225669769514	42.454268759386636	42.929278312776006	43.37304606905392	43.859714337274205	44.42338073358562	44.65987467711081	44.9814993281134	45.38402821385245	45.40830645267432	45.62169607624446	46.22335016155107	46.29582421752576	46.50514447377482	46.91765537366781	47.10284902343331	47.394856140890155	47.894894568911'
coast = np.array(coast_txt.split(),dtype = np.float).ravel()
x = np.arange(coast.size)
coast_x = x
zero_dis = 50#水流衰减距离
damp_factor = 0.01 
damp_b = 0.5/(-1+np.exp(damp_factor*zero_dis))
damp_intercept = 0.5+damp_b
xxx = np.arange(100)
get_weight = lambda dis_input:-damp_b*np.exp(damp_factor*dis_input)+damp_intercept
def get_value(site,site1):
	return np.argmin(np.abs(site-site1))

def norm_v(v1_temp):
	'''单位化'''
	return v1_temp/np.sqrt((v1_temp**2).sum())

def get_euc(x1,x2):
	x1 = np.array(x1)
	x2 = np.array(x2)
	return np.sqrt(((x1-x2)**2).sum())

def filt_points(points,distance = 'each',f = np.median,factor =  3 ):
	'''基于3sigma准则进行滤去异常点
	distance :
	euc ： 基于欧式距离进行过滤
	each： 基于每一维，有一维不正常即不正常，未编写
	factor    :σ原则的系数'''
	if distance  == 'euc':
		center = np.mean(points,axis = 0)
		dis_ls = [get_euc(i,center) for i in points]
		dis_mean = f(dis_ls)
		dis_std = np.std(dis_ls)
		site_anormal = []
		site_abnormal = []
		for i in range(points.shape[0]):
			if  (dis_ls[i]-dis_mean)<factor*dis_std:
				site_anormal.append(i)
			else:
				site_abnormal.append(i)
		return points[site_anormal,:],points[site_abnormal,:]
	elif distance == 'each':
		center = np.mean(points,axis = 0)
		std = np.std(points,axis = 0 )
		site_anormal = []
		site_abnormal = []
		for i in range(points.shape[0]):
			if ((points[i][0]-center[0])<factor*std[0] and (points[i][1]-center[1])<factor*std[1]):
				site_anormal.append(i)
			else:
				site_abnormal.append(i)
		return points[site_anormal,:],points[site_abnormal,:]

def interp_for_under_coast(x_i,coast_i,x3,y3):
	range_31 = sorted([x_i,x3])
	range_31 = np.arange(np.ceil(range_31[0]),np.floor(range_31[1]))
	x_interp_31 = np.array([x_i,x3])
	y_interp_31 = np.array([coast_i,y3])
	y_interp_31 = y_interp_31[np.argsort(x_interp_31)]
	x_interp_31 = x_interp_31[np.argsort(x_interp_31)]
	interp_31 = np.interp(range_31,x_interp_31,y_interp_31)
	return range_31,interp_31

def cross_esi(direction = '东北风'):
	'''cross east sea island'''
	damp = 1 

	tan = (coast[1:]-coast[:-1])/(x[1:]-x[:-1]+1e-16)#海岸线切线正切值（无问题）

	if direction == '东北风':
		vx = -np.ones(x.shape)
		vy = vx
	elif direction == '东南风':
		vx = -np.ones(x.shape)
		vy = np.ones(x.shape)
	elif direction == '西北风':
		vx =  np.ones(x.shape)
		vy = -np.ones(x.shape)
	elif direction == '西南风':
		vx = vy = np.ones(x.shape)
	elif direction == '西风':
		vx = np.ones(x.shape)
		vy = np.zeros(x.shape)
	elif direction == '北风':
		vx = np.zeros(x.shape)
		vy = -np.ones(x.shape)
	elif direction == '南风':
		vx = np.zeros(x.shape)
		vy = np.ones(x.shape)
	elif direction == '东风':
		vx = -np.ones(x.shape)
		vy = np.zeros(x.shape)
	else:
		print('您输入的风向暂时不支持')
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

	theta_c = np.arctan(tan)
	v1 = np.array((np.cos(theta_c),np.sin(theta_c))).T
	v2 = np.array((np.cos(theta_c+0.5*np.pi),np.sin(theta_c+0.5*np.pi))).T
	v3 = np.array((vx,vy)).T
	theta_13 = []
	for i in range(v3.shape[0]):
		theta_13_t=np.arccos(np.dot(v1[i],v3[i])/np.sqrt((v1[i]**2).sum()+(v3[i]**2).sum()))
		theta_13.append(theta_13_t)
		v1_temp=-v1[i]#v1反方向向量
		v1_temp=v1_temp/np.sqrt((v1_temp**2).sum()) #v1_temp是v1反向量的单位化
		v2_temp = norm_v(v2[i])#v2单位化
		v3_temp=v3[i]/np.sqrt((v3[i]**2).sum())#v3单位化
		if (v1[i][0]>=0 and v1[i][1]>=0):
			#if(v3[i][0]<=0 and v3[i][1]>=0):#   =是否能取到，何时取到，先凭感觉的，都取并没有影响
			if -1<=v3_temp[0]<=v2_temp[0] and v3_temp[1]>=0:
				theta_w2 = theta_c[i]-theta_13
			if -1<=v3_temp[0]<=v1_temp[0] and v3_temp[1]<=0:
				theta_w2 = theta_c[i]-theta_13
			if v1_temp[0]<=v3_temp[0]<=1 and v3_temp[1]<=0:
				theta_w2 = theta_c[i]+theta_13
			if -v1_temp[0]<=v3_temp[0]<=1 and v3_temp[1]>=0:
				theta_w2 = theta_c[i]+theta_13
			if v2_temp[0]<=v3_temp[0]<=-v1_temp[0] and v3_temp[1]>=0:
				theta_w2 = theta_c[i]-theta_13
		if v1[i][0]>=0 and v1[i][1]<=0:
			if -1<=v3_temp[0]<=-v1_temp[0] and v3_temp[1]<=0:
				theta_w2 = theta_c[i]+theta_13
			if -1<=v3_temp[0]<=v1_temp[0] and v3_temp[1]>=0:
				theta_w2 = theta_c[i]+theta_13
			if v1_temp[0]<=v3_temp[0]<=1 and v3_temp[1]>=0:
				theta_w2 = theta_c[i]-theta_13
			if -v1_temp[0]<=v3_temp[0]<=1 and v3_temp[1]<=0:
				theta_w2 = theta_c[i]-theta_13
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
			range_31,interp_31 = interp_for_under_coast(x[i],coast[i],x3,y3)
			range_32,interp_32 = interp_for_under_coast(x[j],coast[j],x3,y3)
			'''存在的bug：交点超出海岸线的坐标范围'''
			site_31_temp = np.where((range_31>=x.min())&(range_31<=x.max()))[0]
			site_32_temp = np.where((range_32>=x.min())&(range_32<=x.max()))[0]
			if site_31_temp.size == 0 :
				bool_under_coast_31 = 0 
			else:
				interp_31 = interp_31[site_31_temp]
				range_31 = range_31[site_31_temp]
				coast_range_31 = coast[np.where((x>=range_31.min())&(x<=range_31.max()))]
				bool_under_coast_31 = (interp_31<coast_range_31).any()#修正，不能用any()
			if site_32_temp.size == 0 :
				bool_under_coast_32 = 0 
			else:
				interp_32 = interp_32[np.where((range_32>=x.min())&(range_32<=x.max()))]
				range_32 = range_32[np.where((range_32>=x.min())&(range_32<=x.max()))]
				coast_range_32 = coast[np.where((x>=range_32.min())&(x<=range_32.max()))]
				bool_under_coast_32 = (interp_32<coast_range_32).any()
			if bool_under_coast_31 or bool_under_coast_32 :
				continue
		
			#trash_m.append(v[i]+v[j])#水的输送量，但是水速越快，垃圾越不容易留下来

			weight_1 = get_weight(get_euc([x[i],coast[i]],[x3,y3]))
			weight_2 = get_weight(get_euc([x[j],coast[j]],[x3,y3]))
			if weight_1>0 and weight_2>0:
				trash_m.append(weight_1+weight_2)
				crossx_ls.append(x3)
				crossy_ls.append(y3)

			
	return np.array(crossx_ls),np.array(crossy_ls),trash_m