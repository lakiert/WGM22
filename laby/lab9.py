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


plt.figure(figsize=(16, 8))
plt.subplot(1, 3, 1)
plt.title('RGB')
plt.imshow(tryb1)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.title('YCbCr')
plt.imshow(tryb2)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.title('HSV')
plt.imshow(tryb3)
plt.axis('off')
plt.savefig('fig1.png')
plt.show()
