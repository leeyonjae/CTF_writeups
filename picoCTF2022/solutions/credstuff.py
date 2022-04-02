# credstuff solution

pw = "cvpbPGS{P7e1S_54I35_71Z3}"

pw_ord = [ord(c) for c in pw]
print(pw_ord)

for i in range(0,26):
    msg = "Shift %s : " % i
    for x in pw_ord:
        if x in range(65,91):
            msg += chr(((x - 65 + i) % 26) + 65)
        elif x in range(97,123):
            msg += chr(((x - 97 + i) % 26) + 97)
        else:
            msg += chr(x)
    print(msg)
