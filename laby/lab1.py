import sys

from PIL import Image
import numpy as np


# zad 2
# obrazek = Image.open("inicjaly.bmp")
# obrazek.show()
# print("informacje o obrazie")
# print("tryb:", obrazek.mode)
# print("format:", obrazek.format)
# print("rozmiar:", obrazek.size)




# zad 3
# obrazek = Image.open("inicjaly.bmp")
# dane_obrazka = np.asarray(obrazek)
#
# np.set_printoptions(threshold=sys.maxsize)
# dane_obrazka1 = dane_obrazka * 1
# print(dane_obrazka1)
#
# t2_text = open('t2.txt', 'w')
# for rows in dane_obrazka1:
#     for item in rows:
#         t2_text.write(str(item) + ' ')
#     t2_text.write('\n')





# zad 4
# obrazek = Image.open("inicjaly.bmp")
# dane_obrazka = np.asarray(obrazek)
#
# print("typ danych tablicy:", dane_obrazka.dtype)
# print("rozmiar tablicy:", dane_obrazka.shape)
# print("liczba elementow:", dane_obrazka.size)
# print("wymiar tablicy:", dane_obrazka.ndim)
# print("rozmiar wyrazu tablicy:", dane_obrazka.itemsize)
#
# print("piksel o adresie (50, 30):", dane_obrazka[30][50])
# print("piksel o adresie (90, 40):", dane_obrazka[40][90])
# print("piksel o adresie (99, 0):", dane_obrazka[0][99])



# zad 5

# obrazek = Image.open("inicjaly.bmp")
# dane_obrazka = np.asarray(obrazek)
# t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
# print("typ danych inicjaly.txt:", t1.dtype)
# print("typ danych inicjaly.bmp:", dane_obrazka.dtype, '\n')
# print("rozmiar inicjaly.txt:", t1.shape)
# print("rozmiar inicjaly.bmp:", dane_obrazka.shape, '\n')
# print("liczba inicjaly.txt:", t1.size)
# print("liczba inicjaly.bmp:", dane_obrazka.size, '\n')
# print("wymiar inicjaly.txt:", t1.ndim)
# print("wymiar inicjaly.bmp:", dane_obrazka.ndim, '\n')
# print("rozmiar wyrazu inicjaly.txt:", t1.itemsize)
# print("rozmiar wyrazu inicjaly.bmp:", dane_obrazka.itemsize)
#
# porownanie = t1 == dane_obrazka
# czy_rowne = porownanie.all()
# print("czy tablice sa rowne? : ", czy_rowne)


# zad 6

# obrazek = Image.open("inicjaly.bmp")
# dane_obrazka = np.asarray(obrazek)
# t1 = np.loadtxt("inicjaly.txt", dtype=np.int_)
# print("typ danych inicjaly.txt:", t1.dtype)
# print("typ danych inicjaly.bmp:", dane_obrazka.dtype, '\n')
# print("rozmiar inicjaly.txt:", t1.shape)
# print("rozmiar inicjaly.bmp:", dane_obrazka.shape, '\n')
# print("liczba inicjaly.txt:", t1.size)
# print("liczba inicjaly.bmp:", dane_obrazka.size, '\n')
# print("wymiar inicjaly.txt:", t1.ndim)
# print("wymiar inicjaly.bmp:", dane_obrazka.ndim, '\n')
# print("rozmiar wyrazu inicjaly.txt:", t1.itemsize)
# print("rozmiar wyrazu inicjaly.bmp:", dane_obrazka.itemsize)
#
# porownanie = t1 == dane_obrazka
# czy_rowne = porownanie.all()
# print("czy tablice sa rowne? : ", czy_rowne)
#
# ob_d1 = Image.fromarray(t1)
# ob_d1.show()

