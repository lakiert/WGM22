from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt


# zad 1,2

# im1 = Image.open("obraz.jpg")
# T = np.asarray(im1)
# t_r = T[:, :, 0]
# t_g = T[:, :, 1]
# t_b = T[:, :, 2]
# im_r = Image.fromarray(t_r)
# im_g = Image.fromarray(t_g)
# im_b = Image.fromarray(t_b)
#
# im2 = Image.merge('RGB', (im_r, im_g, im_b))
# T2 = np.asarray(im2)
# difference = ImageChops.difference(im1, im2)
#
# im1.show()
# im2.show()
# difference.show()
#
# porownanie = T == T2
# czy_rowne = porownanie.all()
# print(czy_rowne)


# zad 3

# im1 = Image.open("obraz.jpg")
#
# r, g, b = im1.split()
# im3 = Image.merge('RGB', (b, g, r))
#
# im3.save('im3.jpg')
# im3.save('im3.png')
#
# im3_1 = Image.open('im3.jpg')
# im3_2 = Image.open('im3.png')
# difference = ImageChops.difference(im3_1, im3_2)
# difference.show()

# obraz1_1jpg = Image.open('obraz1_1.jpg')
# obraz1_1png = Image.open('obraz1_1.png')
# obraz1_1Njpg = Image.open('obraz1_1N.jpg')
# obraz1_1Npng = Image.open('obraz1_1N.png')
# obraz1_2jpg = Image.open('obraz1_2.jpg')
# obraz1_2png = Image.open('obraz1_2.png')
# obraz1_2Njpg = Image.open('obraz1_2N.jpg')
# obraz1_2Npng = Image.open('obraz1_2N.png')
#
# dif1 = ImageChops.difference(obraz1_1jpg, obraz1_1png)
# dif2 = ImageChops.difference(obraz1_1Njpg, obraz1_1Npng)
# dif3 = ImageChops.difference(obraz1_2jpg, obraz1_2png)
# dif4 = ImageChops.difference(obraz1_2Njpg, obraz1_2Npng)
#
# plt.figure(figsize=(32, 16))
# plt.subplot(2, 2, 1)
# plt.imshow(dif1, "gray")
# plt.axis('off')
# plt.subplot(2, 2, 2)
# plt.imshow(dif2, "gray")
# plt.axis('off')
# plt.subplot(2, 2, 3)
# plt.imshow(dif3, "gray")
# plt.axis('off')
# plt.subplot(2, 2, 4)
# plt.imshow(dif4, "gray")
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig1.png')
# plt.show()


# zad 4

# def create_tab(h, w, dzielnik):
#     t = (h, w)
#     tab = np.zeros(t, dtype=np.uint8)
#     grubosc = int(min(w, h) / dzielnik)
#     ile = int(min(w, h) / (2*grubosc))
#
#     for i in range(ile+1):
#
#         if i % 2 == 0:
#             z1 = h - i*grubosc
#             z2 = w - i*grubosc
#             tab[i*grubosc:z1, i*grubosc:z2] = h/2
#         else:
#             z1 = h - i*grubosc
#             z2 = w - i*grubosc
#             tab[i*grubosc:z1, i*grubosc:z2] = w/2
#
#     return tab
#
#
#
# T = create_tab(1050, 700, 15)
# T_im = Image.fromarray(T)
#
# im4 = Image.open('obraz.jpg')
# r, g, b = im4.split()
#
# e1 = Image.merge('RGB', (T_im, g, b))
# e2 = Image.merge('RGB', (r, T_im, b))
# e3 = Image.merge('RGB', (r, g, T_im))
#
#
# plt.figure(figsize=(32, 16))
# plt.subplot(1, 3, 1)
# plt.imshow(e1)
# plt.axis('off')
# plt.subplot(1, 3, 2)
# plt.imshow(e2)
# plt.axis('off')
# plt.subplot(1, 3, 3)
# plt.imshow(e3)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig2.png')
# plt.show()



# zad 5

# def create_obraz(x1, x2, y1, y2):
#     tab = np.zeros((300, 300), dtype=np.uint8)
#
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             tab[i, j] = 255
#
#     img = Image.fromarray(tab)
#     return img
#
#
# img1 = create_obraz(75, 225, 75, 225)
# img2 = create_obraz(0, 300, 125, 175)
# img3 = create_obraz(125, 175, 0, 300)
#
#
# image1 = Image.merge('RGB', (img1, img2, img3))
# image2 = Image.merge('RGB', (img1, img3, img2))
# image3 = Image.merge('RGB', (img2, img1, img3))
# image4 = Image.merge('RGB', (img2, img3, img1))
# image5 = Image.merge('RGB', (img3, img1, img2))
# image6 = Image.merge('RGB', (img3, img2, img1))
#
# plt.figure(figsize=(32, 16))
# plt.subplot(3, 2, 1)
# plt.imshow(image1)
# plt.axis('off')
# plt.subplot(3, 2, 2)
# plt.imshow(image2)
# plt.axis('off')
# plt.subplot(3, 2, 3)
# plt.imshow(image3)
# plt.axis('off')
# plt.subplot(3, 2, 4)
# plt.imshow(image4)
# plt.axis('off')
# plt.subplot(3, 2, 5)
# plt.imshow(image5)
# plt.axis('off')
# plt.subplot(3, 2, 6)
# plt.imshow(image6)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig3.png')
# plt.show()

