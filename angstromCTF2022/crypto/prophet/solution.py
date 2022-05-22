import datetime

rns = open("./chall.txt", "r")

lines = [int(i.strip()) for i in rns.readlines()[4:]]
flags = [4301770859063564088, 3588343789060400015, 16743982520636489794, 14486217089676259227]
flag = ""

record = dict()

# print(len(bin(flag[2])) - 2)
# 64


for i in range(len(flags)):
    b = bin(flags[i])[2:]
    print("0" * (64 - len(b)) + b)





nbits = 64
rn = 0
gap = 0
for i in range(100000):
    pass

for j in range(4):
    e = flags[j] ^ rn

ind = 100004

for k in range(len(lines)):
    record[ind] = lines[k]
    if gap < 2:
        b = bin(lines[k])[2:]
        print(ind, ":", "0" * (64 - len(b)) + b)
    ind += 1
    for l in range(gap):
        ind += 1
    gap = (gap + 1) % 13
