img = imread('湛江湾1.png');
imshow(img)
site = (img(:,:,1)==174).*...
    (img(:,:,2)==220).*...
    (img(:,:,3)==252);
img = rgb2gray(img);
img(find(~site))=0;
img(find(site))=255;
%imshow(img)
title('raw')

i2=im2bw(img);    %二值化搜索
i3 = bwmorph(i2,'close');  %闭运算
% figure
% imshow(i3)
% title('close')
i4 = bwmorph(i2,'open');  %开运算
figure(1)
imshow(i4)
% title('open')
%bwmorph还支持类似bothat 
%tophat thin等操作个体看下help参数

save('map_zj','i4');
img = i4;