# !/usr/bin/python3
# coding: utf-8
# @author: Deng Junwei
# @date: 2019/4/10
# @institute:SJTU
import cv2
from PIL import Image
import random
a = list(range(500))
random.shuffle(a)
for i in range(40):
    if i < 125:
        img_ori = cv2.imread('1000002477_{}.png'.format(a[i]+1))
    elif i < 250:
            img_ori = cv2.imread('1000003222_{}.png'.format(a[i]+1))
    elif i < 375:
        img_ori = cv2.imread('t18-01144_{}.png'.format(a[i]+1))
    elif i < 500:
        img_ori = cv2.imread('t18-01516_{}.png'.format(a[i]+1))
    img_cut = img_ori[138:638, 138:638, :]
    img_cut = img_cut[:,:,::-1]
    im = Image.fromarray(img_cut)
    if i < 125:
        im.save('F:/BIBM/testcase/newimage/1000002477_{}-mask.png'.format(a[i]+1))
    elif i < 250:
        im.save('F:/BIBM/data_cache/overall_dataset/image/1000003222_{}-mask.png'.format(a[i]+1))
    elif i < 375:
        im.save('F:/BIBM/data_cache/overall_dataset/image/t18-01144_{}-mask.png'.format(a[i]+1))
    elif i < 500:
        im.save('F:/BIBM/data_cache/overall_dataset/image/t18-01516_{}-mask.png'.format(a[i]+1))
