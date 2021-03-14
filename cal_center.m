%！！！由于tan是个函数，不能作为变量
%！！！所以python里的变量tan改为tan_，多了个下划线！！！
damp = 1; 
x = 0:9;
coast = sin(0.5*x);
tan_ = (coast(2:end)-coast(1:end-1))./(x(2:end)-x(1:end-1)+1e-16);
vx = 0.5*(x.^2)+1;
vx = -vx;
vy = -abs(vx);
vx = vx(1:end-1);
vy = vy(1:end-1);

v = (vx.^2+vy.^2).^(0.5);
theta_w1 = atan(vy./(vx+1e-16));
minus_pi_site = find((vx<0)& (vy<0));
theta_w1(minus_pi_site) = theta_w1(minus_pi_site)-pi;
plus_pi_site = find((vx<0)&(vy>0));
theta_w1(plus_pi_site) = theta_w1(plus_pi_site)+pi;
theta_c = atan(tan_);
theta_temp = 0.25*pi+theta_c-theta_w1;
theta_w2 = abs(theta_temp)+abs(theta_c)-0.5*pi;
v_2 = v.*damp;

crossx = zeros(numel(theta_w2));
crossy = zeros(numel(theta_w2));
crossx_ls = [];
crossy_ls = [];
trash_m = [];
for i = 1:numel(theta_w2)
    theta_1 = theta_w2(i);
    for j = (i+1):numel(theta_w2)
        theta_2 = theta_w2(j);
        x3 = (coast(i)-coast(j)-tan(theta_1).*x(i)+tan(theta_2).*x(j))./(tan(theta_2)-tan(theta_1));
        y3 = coast(j)+(x3-x(j)).*tan(theta_2);
        crossx(i,j) = x3;
        crossy(i,j) = y3;
        vec_x3 = [x3,y3];
        vec_x2 = [x(j),coast(j)];
        vec_x32 = vec_x2-vec_x3;
        if dot(vec_x32,[cos(theta_w2(j)),sin(theta_w2(j))])>0
            continue ;
        end
        crossx_ls = [crossx_ls,x3];
        crossy_ls = [crossy_ls,y3];
    end
end
plot(x,coast);
hold on ;
plot(crossx_ls,crossy_ls,'r.');