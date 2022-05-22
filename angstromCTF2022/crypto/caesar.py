import string

flagc = "sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}"
offset = ord('a')
flag = ""

for i in range(26):
    out = ""
    for c in flagc:
        if c in string.ascii_lowercase:
            out += chr((((ord(c) - offset) + i) % 26) + offset)
        else:
            out += c
        
    if out[0:4] == "actf":
        flag = out
        print(i)
        break

print(flag)