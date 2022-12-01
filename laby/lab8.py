from PIL import Image, ImageFilter
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


# zad 1, 2

image = Image.open('obraz.jpg')
print(image.mode)
im = image.convert('L')
print(im.mode)


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


# statystyki(im)
hist = im.histogram()
plt.title("histogram")
plt.plot(range(256), hist[:256], color='b')
# plt.show()



# zad 3


def histogram_norm(obraz):
    histogram = obraz.histogram()
    width, height = obraz.size
    ilosc_pikseli = width*height
    hist_norm = histogram

    for i in range(0, 256):
        hist_norm[i] = histogram[i] / ilosc_pikseli

    return hist_norm


hist_norm = histogram_norm(im)
# print(hist_norm)
# plt.title("histogram znormalizowany")
# plt.plot(range(256), hist_norm[:256], color='b')
# plt.show()



# zad 4


def histogram_cumul(im):
    hist_norm = histogram_norm(im)
    hist_kumul = [0] * 256

    for i in range(0, 256):
        for j in range(0, i+1):
            hist_kumul[i] += hist_norm[j]

    return hist_kumul


hist_kumul = histogram_cumul(im)
# print(hist_kumul)

plt.title("histogram skumulowany")
plt.plot(range(256), hist_kumul[:256], color='b')
# plt.show()



# zad 5

def histogram_equalization(im):
    width, height = im.size

    piksele = np.asarray(im)
    piksele2 = piksele.copy()

    hist_kumul = histogram_cumul(im)

    for i in range(0, height):
        for j in range(0, width):
            piksele2[i][j] = int(255*hist_kumul[piksele2[i][j]])

    nowy_obraz = Image.fromarray(piksele2)
    return nowy_obraz

equalized = histogram_equalization(im)
equalized.save("equalized.jpg")
eq_his = equalized.histogram()

plt.title("histogram - po wyrównaniu")
plt.bar(range(256), eq_his[:256], color='b')
# plt.show()


# zad 6

equalized1 = ImageOps.equalize(im)
equalized1.save("equalized1.jpg")

# zad 6.1

difference = ImageChops.difference(equalized, equalized1)
# difference.show()


# zad 6.2


hist2 = equalized.histogram()
hist3 = equalized1.histogram()


# plt.subplot(2, 1, 1)
# plt.title("histogram - funkcja napisana przeze mnie")
# plt.plot(range(256), hist2[:256], color='b')
# plt.subplot(2, 1, 2)
# plt.title("histogram - funkcja ImageOps.equalize()")
# plt.plot(range(256), hist3[:256], color='r')
# plt.tight_layout(pad=5)
# plt.show()


plt.title("porównanie histogramów")
plt.plot(range(256), hist2[:256], color='b')
plt.plot(range(256), hist3[:256], color='r')
# plt.show()


# zad 6.3

# print("\n\nstatystyki dla equalized: ")
# statystyki(equalized)
# print("\n ------------- ")
# print("\n\nstatystyki dla equalized1: ")
# statystyki(equalized1)




# zad 7


obraz_detail = im.filter(ImageFilter.DETAIL)
obraz_sharpen = im.filter(ImageFilter.SHARPEN)
obraz_contour = im.filter(ImageFilter.CONTOUR)



plt.subplot(2, 2, 1)
plt.title("DETAIL")
plt.imshow(obraz_detail, 'gray')
plt.subplot(2, 2, 2)
plt.title("SHARPEN")
plt.imshow(obraz_sharpen, 'gray')
plt.subplot(2, 2, 3)
plt.title("CONTOUR")
plt.imshow(obraz_contour, 'gray')
plt.subplot(2, 2, 4)
plt.title("WYRÓWNANIE HISTOGRAMU")
plt.imshow(equalized1, 'gray')
plt.tight_layout(pad=2)
plt.savefig("filtry.jpg")
plt.show()
