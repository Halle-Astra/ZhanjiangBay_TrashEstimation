root = './斯格明子数/';
fs = dir('./斯格明子数/*.dat');
res = [];
for i = 1 : length(fs)
    res = [res,dint([root,fs(i).name])];
end
disp(res);