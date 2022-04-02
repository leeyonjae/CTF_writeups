# basic-mod1 solution

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

enc = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288"
deci = enc.split(" ")

res = ""
for i in deci:
    res += chars[(int(i) % 37)] 

print(res)