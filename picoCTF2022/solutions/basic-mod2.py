# basic-mod2 Solution

chars = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_" # charset starts at 1, not 0; first char is fodder

enc = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186"
deci = enc.split(" ")

# Mod 41
decmod = [int(i) % 41 for i in deci]

# Modular Inverse Function
def modinv(a,m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return 0

# Find Modular Inverses
modres = [modinv(d, 41) for d in decmod]

# Map to the charset
res = ""
for d in modres:
    res += chars[d % 38] 

print(res)