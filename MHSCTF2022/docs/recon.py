# Solution for the problem "Reconstruction"

import numpy as np
from PIL import Image, ImageDraw

colorfile = open("recon.txt", "r")

untreated = colorfile.read()
treated = untreated.split(",")

nums = []
w = 0
h = 0

for val in treated:
    if val == ";":
        h += 1
        w = int(w / 3)
        break
    elif val[0] == ";":
        h += 1
        nums.append(val[1:])
    else:
        if h == 0:
            w += 1
        nums.append(val)



a = np.array(nums, dtype=np.uint8).reshape((w, h, 3))

img = Image.fromarray(a,'RGB').transpose(Image.FLIP_LEFT_RIGHT)

out = img.transpose(Image.ROTATE_90)

out.save("recon.png", bitmap_format='png')
