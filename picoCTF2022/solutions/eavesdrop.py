# eavesdrop file writing script

code = "53 61 6c 74 65 64 5f 5f f1 a4 a6 81 bf d0 ca d4 85 9b 95 1d 3d 61 ca 1d f9 a2 8d 5a f0 c9 18 00 14 15 7f e0 a9 c4 46 38 0b a1 76 f2 3c 38 45 59".split(" ")

enc = open("../sources/file.des3", "wb")

si = [bytes.fromhex(i) for i in code]
s = b''
for i in si:
    s += i

enc.write(s)
