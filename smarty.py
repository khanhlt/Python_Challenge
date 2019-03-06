from PIL import Image
from numpy import *

img = asarray(Image.open('oxygen.png'))
h = img.shape[0]//2
width = img.shape[1]

print(''.join(chr(img[h][i][0]) for i in range(0, width, 7)))

print(''.join(chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]))