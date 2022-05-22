confetti = open("./confetti.png", "rb").read().split(b'\x89PNG')

for i in range(1, len(confetti)):
    out = open("./confetti" + str(i) + ".png", "wb")
    res = b'\x89PNG' + confetti[i]
    out.write(res)
    out.close()

