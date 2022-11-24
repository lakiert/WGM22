from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("obraz.jpg")


# zad 1

def filtruj(obraz, kernel, scale):
    im1 = obraz.copy()
    w, h = obraz.size
    pixele1 = obraz.load()
    pixele2 = im1.load()
    dlugosc = len(kernel)
    d = int(dlugosc / 2)

    for i in range(d, w - d):
        for j in range(d, h - d):
            help = [0, 0, 0]
            for x in range(dlugosc):
                for y in range(dlugosc):
                    x1 = i + x - d
                    y1 = j + y - d
                    pix = pixele1[x1, y1]
                    help[0] += pix[0] * kernel[x][y]
                    help[1] += pix[1] * kernel[x][y]
                    help[2] += pix[2] * kernel[x][y]
            pixele2[i, j] = (int(help[0] / scale), int(help[1] / scale), int(help[2] / scale))
    return im1


# zad 2


# print(ImageFilter.BLUR.filterargs)
# blur_kernel = [[1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1]]
# blur_scale = 16
#
# blur = filtruj(im, blur_kernel, blur_scale)
# blur1 = im.filter(ImageFilter.BLUR)
# difference = ImageChops.difference(blur1, blur)
#
# plt.figure(figsize=(16, 8))
# plt.subplot(1, 3, 1)
# plt.imshow(blur)
# plt.axis('off')
# plt.subplot(1, 3, 2)
# plt.imshow(blur1)
# plt.axis('off')
# plt.subplot(1, 3, 3)
# plt.imshow(difference)
# plt.axis('off')
# plt.savefig('fig1.png')
# plt.show()


# zad 3


# im_l = im.convert('L')
#
# print(ImageFilter.EMBOSS.filterargs)
# sobel1 = (-1, 0, 1, -2, 0, 2, -1, 0, 1)
# sobel2 = (-1, -2, -1, 0, 0, 0, 1, 2, 1)
#
# ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, 0, 1, -2, 0, 2, -1, 0, 1))
# im_l1 = im.filter(ImageFilter.EMBOSS)
#
# ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, -2, -1, 0, 0, 0, 1, 2, 1))
# im_l2 = im.filter(ImageFilter.EMBOSS)
#
# plt.figure(figsize=(16, 8))
# plt.subplot(1, 3, 1)
# plt.imshow(im_l, 'gray')
# plt.axis('off')
# plt.subplot(1, 3, 2)
# plt.imshow(im_l1)
# plt.axis('off')
# plt.subplot(1, 3, 3)
# plt.imshow(im_l2)
# plt.axis('off')
# plt.savefig('fig2.png')
# plt.show()


# zad 4

# im2 = im.filter(ImageFilter.DETAIL)
# dif2 = ImageChops.difference(im, im2)
# im4 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
# dif4 = ImageChops.difference(im, im4)
# im6 = im.filter(ImageFilter.SHARPEN)
# dif6 = ImageChops.difference(im, im6)
# im8 = im.filter(ImageFilter.SMOOTH_MORE)
# dif8 = ImageChops.difference(im, im8)

# plt.subplot(4, 2, 1)
# plt.imshow(im2)
# plt.title("DETAIL")
# plt.axis('off')
# plt.subplot(4, 2, 2)
# plt.imshow(dif2)
# plt.axis('off')
# plt.subplot(4, 2, 3)
# plt.imshow(im4)
# plt.title("EDGE_ENHANCE_MORE")
# plt.axis('off')
# plt.subplot(4, 2, 4)
# plt.imshow(dif4)
# plt.axis('off')
# plt.subplot(4, 2, 5)
# plt.imshow(im6)
# plt.title("SHARPEN")
# plt.axis('off')
# plt.subplot(4, 2, 6)
# plt.imshow(dif6)
# plt.axis('off')
# plt.subplot(4, 2, 7)
# plt.imshow(im8)
# plt.title("SMOOTH_MORE")
# plt.axis('off')
# plt.subplot(4, 2, 8)
# plt.imshow(dif8)
# plt.axis('off')
# plt.subplots_adjust(wspace=0, hspace=0.5)
# plt.savefig('fig3.png')
# plt.show()


# zad 4 b

#
# im11 = im.filter(ImageFilter.BoxBlur(5))
# dif11 = ImageChops.difference(im, im11)
# im12 = im.filter(ImageFilter.GaussianBlur(radius=2))
# dif12 = ImageChops.difference(im, im12)
# im13 = im.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
# dif13 = ImageChops.difference(im, im13)
# im14 = im.filter(ImageFilter.Kernel(size=(3, 3), kernel=(-1, -1, -1, -1, 9, -1, -1, -1, -1), scale=None, offset=0))
# dif14 = ImageChops.difference(im, im14)
# im15 = im.filter(ImageFilter.RankFilter(size=3, rank=0))
# dif15 = ImageChops.difference(im, im15)
# im16 = im.filter(ImageFilter.MedianFilter(size=3))
# dif16 = ImageChops.difference(im, im16)
# im17 = im.filter(ImageFilter.MinFilter(size=3))
# dif17 = ImageChops.difference(im, im17)
# im18 = im.filter(ImageFilter.MaxFilter(size=3))
# dif18 = ImageChops.difference(im, im18)
#
#
# plt.figure(figsize=(16,8))
# plt.subplot(8, 2, 1)
# plt.imshow(im11)
# plt.title("BoxBlur")
# plt.axis('off')
# plt.subplot(8, 2, 2)
# plt.imshow(dif11)
# plt.axis('off')
# plt.subplot(8, 2, 3)
# plt.imshow(im12)
# plt.title("GaussianBlur")
# plt.axis('off')
# plt.subplot(8, 2, 4)
# plt.imshow(dif12)
# plt.axis('off')
# plt.subplot(8, 2, 5)
# plt.imshow(im13)
# plt.title("UnsharpMask")
# plt.axis('off')
# plt.subplot(8, 2, 6)
# plt.imshow(dif13)
# plt.axis('off')
# plt.subplot(8, 2, 7)
# plt.imshow(im14)
# plt.title("Kernel")
# plt.axis('off')
# plt.subplot(8, 2, 8)
# plt.imshow(dif14)
# plt.axis('off')
# plt.subplot(8, 2, 9)
# plt.imshow(im15)
# plt.title("RankFilter")
# plt.axis('off')
# plt.subplot(8, 2, 10)
# plt.imshow(dif15)
# plt.axis('off')
# plt.subplot(8, 2, 11)
# plt.imshow(im16)
# plt.title("MedianFilter")
# plt.axis('off')
# plt.subplot(8, 2, 12)
# plt.imshow(dif16)
# plt.axis('off')
# plt.subplot(8, 2, 13)
# plt.imshow(im17)
# plt.title("MinFilter")
# plt.axis('off')
# plt.subplot(8, 2, 14)
# plt.imshow(dif17)
# plt.axis('off')
# plt.subplot(8, 2, 15)
# plt.imshow(im18)
# plt.title("MaxFilter")
# plt.axis('off')
# plt.subplot(8, 2, 16)
# plt.imshow(dif18)
# plt.axis('off')
# plt.subplots_adjust(wspace=0, hspace=0.5)
# plt.savefig('fig4.png')
# plt.show()
