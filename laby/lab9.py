from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt


# zad 1

obraz1 = Image.open("obraz1.png")
# obraz1.show()

obraz2 = obraz1.convert('RGB')
# obraz2.show()

r, g, b, a = obraz1.split()
obraz3 = Image.new('RGB', obraz1.size, (255,255,255))
obraz3.paste(obraz1, (0, 0), a)
# obraz3.show()
# obraz3.save("obraz3.png")

difference = ImageChops.difference(obraz2, obraz3)
# difference.show()




# zad 2

tryb1 = obraz3.convert('CMYK')
tryb2 = obraz3.convert('YCbCr')
tryb3 = obraz3.convert('HSV')


# plt.figure(figsize=(16, 8))
# plt.subplot(1, 3, 1)
# plt.title('RGB')
# plt.imshow(tryb1)
# plt.axis('off')
# plt.subplot(1, 3, 2)
# plt.title('YCbCr')
# plt.imshow(tryb2)
# plt.axis('off')
# plt.subplot(1, 3, 3)
# plt.title('HSV')
# plt.imshow(tryb3)
# plt.axis('off')
# plt.savefig('fig1.png')
# plt.show()


# c, m, y, k = tryb1.split()
# plt.figure()
# plt.subplot(1, 4, 1)
# plt.title('C')
# plt.imshow(c, 'gray')
# plt.axis('off')
# plt.subplot(1, 4, 2)
# plt.title('M')
# plt.imshow(m, 'gray')
# plt.axis('off')
# plt.subplot(1, 4, 3)
# plt.title('Y')
# plt.imshow(y, 'gray')
# plt.axis('off')
# plt.subplot(1, 4, 4)
# plt.title('K')
# plt.imshow(k, 'gray')
# plt.axis('off')
# plt.savefig('cmyk.png')
# plt.show()


# y1, cb, cr = tryb2.split()
# plt.figure()
# plt.subplot(1, 3, 1)
# plt.title('Y')
# plt.imshow(y1, 'gray')
# plt.axis('off')
# plt.subplot(1, 3, 2)
# plt.title('Cb')
# plt.imshow(cb, 'gray')
# plt.axis('off')
# plt.subplot(1, 3, 3)
# plt.title('Cr')
# plt.imshow(cr, 'gray')
# plt.axis('off')
# plt.savefig('ycbcr.png')
# plt.show()


# h, s, v = tryb3.split()
# plt.figure()
# plt.subplot(1, 3, 1)
# plt.title('H')
# plt.imshow(h, 'gray')
# plt.axis('off')
# plt.subplot(1, 3, 2)
# plt.title('S')
# plt.imshow(s, 'gray')
# plt.axis('off')
# plt.subplot(1, 3, 3)
# plt.title('V')
# plt.imshow(v, 'gray')
# plt.axis('off')
# plt.savefig('hsv.png')
# plt.show()




# zad 3

obraz4 = Image.open("obraz4.png")
tlo = obraz4.resize(obraz1.size, 1)

tlo2 = tlo.copy()
tlo2.paste(obraz1, (0, 0), a)

obraz1kopia = obraz1.copy()
obraz1kopia.paste(tlo, (0, 0), a)

# plt.subplot(1, 2, 1)
# plt.imshow(tlo2)
# plt.axis('off')
# plt.subplot(1, 2, 2)
# plt.imshow(obraz1kopia)
# plt.axis('off')
# plt.savefig('fig2.png')
# plt.show()



