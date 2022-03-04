# Solution code for the problem "Green"
from pathlib import Path
from PIL import Image
import numpy as np

with Image.open(Path("green.png")) as img:
    w = img.width
    h = img.height

    #print(w, "x", h)
    #print(img.getpixel((11,0)))

    greens = []
    for x in range(0, w):
        p = img.getpixel((x, 0))
        greens.append(p[1])

    text = ""

    frq = []

    for i in greens:
        text = text + chr(i)

    for t in text:
        if t not in frq:
            frq.append(t)

    
    print(text)