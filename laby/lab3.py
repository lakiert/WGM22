from PIL import Image
import numpy as np
import random


# zad 1

# def create_obraz1(h, w, dzielnik, k1, k2):
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
#             tab[i*grubosc:z1, i*grubosc:z2] = k1
#         else:
#             z1 = h - i*grubosc
#             z2 = w - i*grubosc
#             tab[i*grubosc:z1, i*grubosc:z2] = k2
#
#     return tab
#
#
# def create_obraz4(h, w, wsp, k1, k2):
#     t = (h, w)
#     tab = np.zeros(t, dtype=np.uint8)
#     for i in range(0, h):
#         for j in range(0, w):
#             ran = random.randint(0, wsp)
#             if ran == 0:
#                 tab[i][j] = k1
#             else:
#                 tab[i][j] = k2
#
#     return tab
#
#
# def negatyw_szare(tab):
#     h, w = tab.shape
#     tab_neg = tab.copy()
#     for i in range(h):
#         for j in range(w):
#             tab_neg[i, j] = 255 - tab[i, j]
#     return tab_neg
#
# #tworze obraz 1
# obraz1 = create_obraz1(320, 480, 8, 100, 200)
# obraz1_1 = Image.fromarray(obraz1)
# obraz1_1.save("obraz1_1.jpg")
# obraz1_1.save("obraz1_1.png")
#
# #negatyw obrazu 1
# obraz1_N = negatyw_szare(obraz1)
# obraz1_1N = Image.fromarray(obraz1_N)
# obraz1_1N.save("obraz1_1N.png")
# obraz1_1N.save("obraz1_1N.jpg")
#
# # tworze obraz 2
# obraz2 = create_obraz4(100, 200, 30, 100, 200)
# obraz1_2 = Image.fromarray(obraz2)
# obraz1_2.save("obraz1_2.jpg")
# obraz1_2.save("obraz1_2.png")
#
# # negatyw obrazu 2
# obraz2_N = negatyw_szare(obraz2)
# obraz1_2N = Image.fromarray(obraz2_N)
# obraz1_2N.save("obraz1_2N.png")
# obraz1_2N.save("obraz1_2N.jpg")



# zad 2


# def rysuj_pasy_poziome_3kolory(w, h, dzielnik):
#     t = (h, w, 3)
#     tab = np.ones(t, dtype=np.uint8)
#     grub = int(w / dzielnik)
#     for k in range(dzielnik):
#         for g in range(grub):
#             j = k * grub + g
#             for i in range(h):
#                 if k % 2 == 0:
#                     tab[i, j] = [220, 65, 70]
#                 else:
#                     tab[i, j] = [20, 65, 70]
#     return tab
#
#
# def negatyw(tab):
#     h, w, k = tab.shape
#     tab_neg = tab.copy()
#     for i in range(h):
#         for j in range(w):
#             tab_neg[i, j] = 255 - tab_neg[i, j]
#     return tab_neg
#
# tab1 = rysuj_pasy_poziome_3kolory(300, 200, 10)
# obraz2 = Image.fromarray(tab1)
# obraz2.save('obraz2.jpg')
# obraz2.save('obraz2.png')
#
# obraz_n = negatyw(tab1)
# obraz2_n = Image.fromarray(obraz_n)
# obraz2_n.save('obraz2N.png')
# obraz2_n.save('obraz2N.jpg')




# zad 3

# def paski(obraz):
#     t_obraz = np.asarray(obraz)
#     h, w = t_obraz.shape
#     t =(h, w, 3)
#     tab = np.ones(t, dtype=np.uint8)
#     for i in range(h):
#         for j in range(w):
#             if t_obraz[i, j] == False:
#                 if i % 4 == 0:
#                     tab[i, j] = [100, 130, 200]
#                 elif i % 4 == 1:
#                     tab[i, j] = [100, 130, 200]
#                 elif i % 4 == 2:
#                     tab[i, j] = [200, 30, 100]
#                 else:
#                     tab[i, j] = [200, 30, 100]
#             else:
#                 tab[i, j] = [255, 255, 255]
#     return tab
#
#
# inicjaly = Image.open("inicjaly.bmp")
# obraz = paski(inicjaly)
# obraz3 = Image.fromarray(obraz)
# obraz3.save('obraz3.jpg')
# obraz3.save('obraz3.png')












