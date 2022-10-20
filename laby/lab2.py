from PIL import Image
import numpy as np
import random

# 1

def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    t_obraz_wstawiany = np.asarray(obraz_wstawiany)

    h0, w0 = t_obraz_wstawiany.shape
    rozmiar_tablicy_duzej = (wsp*h0, wsp*w0)
    tab = np.zeros(rozmiar_tablicy_duzej, dtype=int)

    for i in range(h_m, h_m+h0-1):
        for j in range(w_m, w_m+w0-1):
            tab[i][j]=t_obraz_wstawiany[i-h_m][j-w_m]

    tab = tab.astype(bool)
    nowy_obraz=Image.fromarray(tab)
    return nowy_obraz


# 2

# obraz_wstawiany = Image.open("inicjaly.bmp")
#
# nowy_obraz1 = wstaw_obraz(obraz_wstawiany, 50, 25, 2)
# nowy_obraz1.save("inicjaly1.bmp")
#
# nowy_obraz2 = wstaw_obraz(obraz_wstawiany, 10, 10, 3)
# nowy_obraz2.save("inicjaly2.bmp")
#
# nowy_obraz3 = wstaw_obraz(obraz_wstawiany, 290, 140, 4)
# nowy_obraz3.save("inicjaly3.bmp")



# 3

# def create_obraz1(h, w, dzielnik):
#     t = (h, w)
#     tab = np.zeros(t, dtype=int)
#     grubosc = int(min(w, h) / dzielnik)
#     ile = int(min(w, h) / (2*grubosc))
#
#     for i in range(ile+1):
#
#         if i % 2 == 0:
#             z1 = h - i*grubosc
#             z2 = w - i*grubosc
#             tab[i*grubosc:z1, i*grubosc:z2] = 1
#         else:
#             z1 = h - i*grubosc
#             z2 = w - i*grubosc
#             tab[i*grubosc:z1, i*grubosc:z2] = 0
#
#     tab2 = tab.astype(bool)
#     obraz1 = Image.fromarray(tab2)
#     obraz1.save("obraz1.bmp")
#     return tab * 255
#
# obraz1 = create_obraz1(320, 480, 8)
# picture_obraz = Image.fromarray(obraz1)



# def create_obraz2(h, w, dzielnik):
#     t = (h, w)
#     tab = np.ones(t, dtype=int)
#     grub = int(w / dzielnik)
#     print(grub)
#     for k in range(dzielnik):
#         for g in range(grub):
#             i = k * grub + g
#             for j in range(h):
#                 tab[j, i] = k % 2
#     tab2 = tab.astype(bool)
#     print(tab2)
#     obraz = Image.fromarray(tab2)
#     obraz.save("obraz2.bmp")
#
#
# create_obraz2(320, 480, 8)




# def create_obraz3(h, w, m, n):
#     t = (h, w)
#     tab = np.ones(t, dtype=int)
#     print(tab)
#
#     for i in range(n, h-1):
#         for j in range(m, w-1):
#             tab[i, j] = 0
#
#     for i in range(0, n):
#         for j in range(0, m):
#             tab[i, j] = 0
#
#     tab2 = tab.astype(bool)
#     obraz = Image.fromarray(tab2)
#     return obraz
#
# obraz3 = create_obraz3(320,480, 100, 50)
# obraz3.save("obraz3.bmp")




# def create_obraz4(h, w):
#     t = (h, w)
#     tab = np.zeros(t, dtype=int)
#     for i in range(0, h-1):
#         for j in range(0, w-1):
#             tab[i][j] = random.randint(0, 1)
#
#     tab2 = tab.astype(bool)
#     obraz4 = Image.fromarray(tab2)
#     obraz4.save("obraz4.bmp")
#
# create_obraz4(100, 200)


# 4


# def create_obraz4(h, w, wsp):
#     t = (h, w)
#     tab = np.zeros(t, dtype=int)
#     for i in range(0, h-1):
#         for j in range(0, w-1):
#             ran = random.randint(0, wsp)
#             if ran == 0:
#                 tab[i][j] = 1
#             else:
#                 tab[i][j] = 0
#
#
#
#     tab2 = tab.astype(bool)
#     obraz4 = Image.fromarray(tab2)
#     obraz4.save("obraz4.bmp")
#
# create_obraz4(100, 200, 30)