img = imread('տ����1.png');
imshow(img)
site = (img(:,:,1)==174).*...
    (img(:,:,2)==220).*...
    (img(:,:,3)==252);
img = rgb2gray(img);
img(find(~site))=0;
img(find(site))=255;
%imshow(img)
title('raw')

i2=im2bw(img);    %��ֵ������
i3 = bwmorph(i2,'close');  %������
% figure
% imshow(i3)
% title('close')
i4 = bwmorph(i2,'open');  %������
figure(1)
imshow(i4)
% title('open')
%bwmorph��֧������bothat 
%tophat thin�Ȳ������忴��help����

save('map_zj','i4');
img = i4;