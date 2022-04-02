# diffie-hellman solution

# Letter table
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# The Cphertext
ciphertext = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_D9FF6IFD"

# Keygen
p = 13
g = 5
a = 7
b = 3

key = (g ** (a * b)) % p

orig = ""

for c in ciphertext:
    if c in table:
        orig += table[(table.find(c) - key) % 36]
    else:
        orig += c

print(orig)


