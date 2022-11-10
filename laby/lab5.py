from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

# zad 1, 2

# obraz = Image.open("obraz.jpg")
# inicjaly = Image.open("inicjaly.bmp")
#
# def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
#
#     obraz1 = obraz.copy()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if inicjaly.getpixel((i, j)) == 0:
#                 p = obraz.getpixel((i + m, j + n))
#                 obraz1.putpixel((i + m, j + n), (kolor[0], kolor[1], kolor[2]))
#             else:
#                 obraz1.putpixel((i + m, j + n), (255, 255, 255))
#
#     return obraz1
#
#
# obraz1 = wstaw_inicjaly(obraz, inicjaly, 600, 1000, (255, 0, 0))
# obraz1.save("obraz1.jpg")
#
#
# def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
#     obraz1 = obraz.copy()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if inicjaly.getpixel((i, j)) == 0:
#                 p = obraz.getpixel((i + m, j + n))
#                 obraz1.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
#     return obraz1
#
#
# obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, 300, 475, 100, 200, 255)
# obraz2.save("obraz2.jpg")






# zad 3

# obraz = Image.open("obraz.jpg")
# inicjaly = Image.open("inicjaly.bmp")
#
# def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
#     ob = obraz.load()
#     ini = inicjaly.load()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if ini[i,j] == 0:
#                 ob[i + m, j + n] = (kolor[0], kolor[1], kolor[2])
#             else:
#                 ob[i + m, j + n] = (255, 255, 255)
#
#     return ob
#
#
# im3 = obraz.copy()
# wstaw_inicjaly_load(im3, inicjaly, 600, 1000, (255, 0, 0))
# plt.title("wstaw_inicjaly_load")
# plt.axis("off")
# plt.imshow(im3)
# plt.show()



# def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
#     obraz1 = obraz.load()
#     ini = inicjaly.load()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if ini[i, j] == 0:
#                 p = obraz1[i + m, j + n]
#                 obraz1[i + m, j + n] = (p[0] + x, p[1] + y, p[2] + z)
#     return obraz1
#
#
# im4 = obraz.copy()
# wstaw_inicjaly_maska(im4, inicjaly, 300, 475, 100, 100, 100)
# plt.title("wstaw_inicjaly_load")
# plt.axis("off")
# plt.imshow(im4)
# plt.show()



# zad 4

# obraz = Image.open("obraz.jpg")
#
# def kontrast(obraz, wsp_kontrastu):
#     im = obraz.copy()
#     if 0 <= wsp_kontrastu <= 100:
#         mn = ((255 + wsp_kontrastu) / 255) ** 2
#         im = im.point(lambda i: 128 + (i - 128) * mn)
#     return im
#
#
# im4 = obraz.copy()
# im4 = kontrast(im4, 5)
# im5 = obraz.copy()
# im5 = kontrast(im5, 50)
# im6 = obraz.copy()
# im6 = kontrast(im6, 100)
#
# plt.title("kontrast")
# plt.subplot(1, 3, 1)
# plt.axis("off")
# plt.imshow(im4)
# plt.subplot(1, 3, 2)
# plt.axis("off")
# plt.imshow(im5)
# plt.subplot(1, 3, 3)
# plt.axis("off")
# plt.imshow(im6)
# plt.savefig("kontrast_plt")





# obraz = Image.open("obraz.jpg")
#
# def transformacja_logarytmiczna(obraz):
#     im = obraz.copy()
#     im = im.point(lambda i: 255 * np.log(1 + i / 255))
#     return im
#
#
# obraz1 = transformacja_logarytmiczna(obraz)
# plt.title('transformacja_logarytmiczna')
# plt.subplot(1, 2, 1)
# plt.axis('off')
# plt.imshow(obraz)
# plt.subplot(1, 2, 2)
# plt.axis('off')
# plt.imshow(obraz1)
# plt.savefig('transformacja_logarytmiczna')




# obraz = Image.open("obraz.jpg")
#
# def transformacja_gamma(obraz, gamma):
#     im = obraz.copy()
#     if gamma > 0:
#         im = im.point(lambda i: (i / 255) ** (1 / gamma) * 255)
#
#     return im
#
#
# obrazek1 = transformacja_gamma(obraz, 3)
# obrazek2 = transformacja_gamma(obraz, 5)
# obrazek3 = transformacja_gamma(obraz, 10)
#
# plt.title('gamma')
# plt.subplot(1, 3, 1)
# plt.axis('off')
# plt.imshow(obrazek1)
# plt.subplot(1, 3, 2)
# plt.axis('off')
# plt.imshow(obrazek2)
# plt.subplot(1, 3, 3)
# plt.axis('off')
# plt.imshow(obrazek3)
# plt.savefig('gamma')




# zad 4.4

# obraz1 = Image.open("obraz.jpg")
# obraz2 = Image.open("obraz.jpg")
# T = np.array(obraz1, dtype='uint8')
# T += 100
# obraz_wynik1 = Image.fromarray(T, "RGB")
#
# obraz_wynik2 = obraz2.point(lambda i: i + 100)
#
# obraz_wynik1.show()
# obraz_wynik2.show()




# zad 5

# obraz = Image.open("obraz.jpg")
# T = np.array(obraz, dtype='uint8')
# data = T.shape
# h = data[0]
# w = data[1]
#
# for i in range(h):
#     for j in range(w):
#         T[i, j, 0] = (((T[i, j, 0]) / 255) ** (1 / 3) * 255)
#         T[i, j, 1] = (((T[i, j, 1]) / 255) ** (1 / 3) * 255)
#         T[i, j, 2] = (((T[i, j, 2]) / 255) ** (1 / 3) * 255)
#
# obraz_wynik = Image.fromarray(T, "RGB")
# obraz.show()
# obraz_wynik.show()

