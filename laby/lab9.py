from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt


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
difference.show()