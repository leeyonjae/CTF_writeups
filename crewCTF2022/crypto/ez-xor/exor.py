import base64

c = open("./flag.enc", "r").read()
p = base64.b64decode(c)
print(p)
print(len(p))

cmp = b"crew{"

def bxor(b1, b2):
    l = min(len(b1), len(b2))
    xors = []
    for i in range(l):
        xors.append(b1[i] ^ b2[i])

    return xors

print(bxor(p, cmp))

flag = "".join([chr(x ^ 102) for x in p])
print(flag)