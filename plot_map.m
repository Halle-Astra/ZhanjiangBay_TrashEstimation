%提前构造a
%a = xlsread('data.xlsx');
%x = a(:,1);y = a(:,2);z = a(:,3);v1 = a(:,4);
f_z = scatteredInterpolant(x,y,z);%用于插值得到高度
xmin = min(x);xmax = max(x);
ymin = min(y);ymax = max(y);
xx = xmin:xmax;
yy = ymin:ymax;
[X,Y] = meshgrid(xx,yy);
Z = f_z(X,Y);
%f_v = scatteredInterpolant(x,y,z,v1);
%V = f_v(X,Y,Z);
mesh(X,Y,Z)
%figure()
%mesh(X,Y,V)