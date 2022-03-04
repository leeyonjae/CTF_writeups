# Solution code for the problem "1 chal 2 category"
from PIL import Image

# Wacky bit-swap operation
def glorp(n): 
    g = list(format(n, "08b"))                      # n becomes 8-bit binary list
    for i in range(len(g)): # For each bit:
        t = g[i]                                    # temporarily hold i'th bit
        g[i] = g[(i * 332 + 6) % 8]                 # swap with (332i + 6) % 8 th place
        g[(i * 332 + 6) % 8] = t
    return int(''.join(g), 2)

# i -> 332i + 6 % 8
# 0 -> 6 % 8 = 6
# 1 -> 338 % 8 = 2
# 2 -> 670 % 8 = 6 ...


def unglorp(n):
    g = list(format(n,"08b"))
    o = [g[3], g[4], g[1], g[5], g[6], g[7], g[0], g[2]]
    return int(''.join(o),2)

lookup = [unglorp(i) for i in range(256)] # list of 256 glorped nums (0-255)


img = Image.open("encoded.png")
pix = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pix[i, j] = (lookup[pix[i, j][0]], lookup[pix[i, j][1]], lookup[pix[i, j][2]])

img.save("flag.png")
