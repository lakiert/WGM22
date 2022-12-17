from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageEnhance
from PIL import ImageStat as stat

# zad 1

im2 = Image.open("duck.png")
im = im2.convert('RGB')
w, h = im.size
# s_w = 0.15
# s_h = 0.27
# resample_method = ['NEAREST', 'LANCZOS', 'BILINEAR', 'BICUBIC', 'BOX', 'HAMMING']
# im_N = im.resize((int(w * s_w), int(h * s_h)), 0)
# plt.figure(figsize=(8, 64))
#
# i = 1
# for t in range(6):
#     file_name = "resample_" + str(resample_method[t])
#     im_r = im.resize((int(w * s_w), int(h * s_h)), t)
#     plt.subplot(6, 2, i)
#     plt.title(str(file_name))
#     plt.imshow(im_r)
#     plt.axis('off')
#     i += 1
#     diff = ImageChops.difference(im_N, im_r)
#     s = stat.Stat(diff)
#     plt.subplot(6, 2, i)
#     plt.title('srednia' + str(np.round(s.mean, 2)))
#     plt.imshow(diff)
#     plt.axis('off')
#     i += 1
# plt.tight_layout()
# # plt.savefig('fig1.png')
# # plt.show()
#
#
# s_wb = 1 / 0.15
# s_hb = 1 / 0.27
#
# im_0 = im.resize((int(w * s_w), int(h * s_h)), 0)
# im_0b = im_0.resize((int(int(w*s_w) * s_wb), int(int(h*s_h) * s_hb)), 0)
# im_1 = im.resize((int(w * s_w), int(h * s_h)), 1)
# im_1b = im_1.resize((int(int(w*s_w) * s_wb), int(int(h*s_h) * s_hb)), 1)
# im_2 = im.resize((int(w * s_w), int(h * s_h)), 2)
# im_2b = im_2.resize((int(int(w*s_w) * s_wb), int(int(h*s_h) * s_hb)), 2)
# im_3 = im.resize((int(w * s_w), int(h * s_h)), 3)
# im_3b = im_3.resize((int(int(w*s_w) * s_wb), int(int(h*s_h) * s_hb)), 3)
# im_4 = im.resize((int(w * s_w), int(h * s_h)), 4)
# im_4b = im_4.resize((int(int(w*s_w) * s_wb), int(int(h*s_h) * s_hb)), 4)
# im_5 = im.resize((int(w * s_w), int(h * s_h)), 5)
# im_5b = im_5.resize((int(int(w*s_w) * s_wb), int(int(h*s_h) * s_hb)), 5)
#
# # print(im.size, ", ", im_0b.size)
# # print(im.size, ", ", im_1b.size)
# # print(im.size, ", ", im_2b.size)
# # print(im.size, ", ", im_3b.size)
# # print(im.size, ", ", im_4b.size)
# # print(im.size, ", ", im_5b.size)
#
#
# im_skalowany = im.resize((int(int(w*s_w) * s_wb), int(int(h*s_h) * s_hb)), Image.Resampling.NEAREST)
#
#
# plt.figure(figsize=(8, 64))
# plt.subplot(6, 2, 1)
# plt.title('NEAREST')
# plt.imshow(im_0b)
# plt.axis('off')
# plt.subplot(6, 2, 2)
# diff = ImageChops.difference(im_skalowany,im_0b)
# s = stat.Stat(diff)
# plt.title('srednia' + str(np.round(s.mean, 2)))
# plt.imshow(diff)
# plt.axis('off')
# plt.subplot(6, 2, 3)
# plt.title('LANCZOS')
# plt.imshow(im_1b)
# plt.axis('off')
# plt.subplot(6, 2, 4)
# diff = ImageChops.difference(im_skalowany,im_1b)
# s = stat.Stat(diff)
# plt.title('srednia' + str(np.round(s.mean, 2)))
# plt.imshow(diff)
# plt.axis('off')
# plt.subplot(6, 2, 5)
# plt.title('BILINEAR')
# plt.imshow(im_2b)
# plt.axis('off')
# plt.subplot(6, 2, 6)
# diff = ImageChops.difference(im_skalowany,im_2b)
# s = stat.Stat(diff)
# plt.title('srednia' + str(np.round(s.mean, 2)))
# plt.imshow(diff)
# plt.axis('off')
# plt.subplot(6, 2, 7)
# plt.title('BICUBIC')
# plt.imshow(im_3b)
# plt.axis('off')
# plt.subplot(6, 2, 8)
# diff = ImageChops.difference(im_skalowany,im_3b)
# s = stat.Stat(diff)
# plt.title('srednia' + str(np.round(s.mean, 2)))
# plt.imshow(diff)
# plt.axis('off')
# plt.subplot(6, 2, 9)
# plt.title('BOX')
# plt.imshow(im_4b)
# plt.axis('off')
# plt.subplot(6, 2, 10)
# diff = ImageChops.difference(im_skalowany,im_4b)
# s = stat.Stat(diff)
# plt.title('srednia' + str(np.round(s.mean, 2)))
# plt.imshow(diff)
# plt.axis('off')
# plt.subplot(6, 2, 11)
# plt.title('HAMMING')
# plt.imshow(im_5b)
# plt.axis('off')
# plt.subplot(6, 2, 12)
# diff = ImageChops.difference(im_skalowany,im_5b)
# s = stat.Stat(diff)
# plt.title('srednia' + str(np.round(s.mean, 2)))
# plt.imshow(diff)
# plt.axis('off')
# plt.tight_layout()
# plt.savefig('fig2.png')
# # plt.show()


# zad 2

#
# start1 = 271
# start2 = 60
# koniec1 = 543
# koniec2 = 343
# wycinek = (start1, start2, koniec1, koniec2)
# szerokosc_wycinka = wycinek[2] - wycinek[0]
# wysokosc_wycinka = wycinek[3] - wycinek[1]
# skala_szerokosc = 2
# skala_wysokosc = 3
# glowa = im.resize( (skala_szerokosc * szerokosc_wycinka, skala_wysokosc * wysokosc_wycinka), box = wycinek)
#
# glowa1 = im.crop(wycinek)
# w1, h1 = glowa1.size
# glowa1 = glowa1.resize((w1*skala_szerokosc, h1*skala_wysokosc))
#
# diff = ImageChops.difference(glowa, glowa1)
#
# plt.figure()
# plt.subplot(1,3,1)
# plt.title('glowa')
# plt.imshow(glowa)
# plt.axis('off')
# plt.subplot(1,3,2)
# plt.title('glowa1')
# plt.imshow(glowa1)
# plt.axis('off')
# plt.subplot(1,3,3)
# plt.title('roznica')
# plt.imshow(diff)
# plt.axis('off')
# plt.tight_layout()
# plt.savefig('fig3.png')


# zad 3


# rotated_im1 = im.rotate(-60, expand=True, fillcolor=(255, 0, 0))
# rotated_im2 = im.rotate(-60, fillcolor=(255, 0, 0))
# rotated_im3 = im.rotate(60, expand=True, fillcolor=(0, 255, 0))
# rotated_im4 = im.rotate(60, fillcolor=(0, 255, 0))
#
# plt.subplot(2, 2, 1)
# plt.imshow(rotated_im1)
# plt.axis('off')
# plt.subplot(2, 2, 2)
# plt.imshow(rotated_im2)
# plt.axis('off')
# plt.subplot(2, 2, 3)
# plt.imshow(rotated_im3)
# plt.axis('off')
# plt.subplot(2, 2, 4)
# plt.imshow(rotated_im4)
# plt.axis('off')
# plt.tight_layout()
# # plt.show()


# zad 4

#
# w4, h4 = im.size
#
# step1 = im.resize((int(0.5*w4), int(0.5*h4)))
# tlo1 = Image.new('RGB', (w4, h4), (30, 150, 250))
#
# box = (int((w4 - (0.5*w4)))+1, int((h4 - (0.5*h4)))+1)
# tlo1.paste(step1, box)
#
# tlo2 = tlo1.rotate(30, expand=True, fillcolor=(10, 100, 200))
# # tlo2.show()
#


# zad 5


# transposed = im.transpose(Image.TRANSPOSE)  # obrocone w lewo
# transversed = im.transpose(Image.TRANSVERSE)  # obrocone w prawo
#
# im_right = im.transpose(Image.FLIP_LEFT_RIGHT)
# im_right2 = im_right.rotate(-90, expand=True)
#
#
# im_left = im.transpose(Image.FLIP_LEFT_RIGHT)
# im_left2 = im_left.rotate(90, expand=True)
