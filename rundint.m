root = './˹��������/';
fs = dir('./˹��������/*.dat');
res = [];
for i = 1 : length(fs)
    res = [res,dint([root,fs(i).name])];
end
disp(res);