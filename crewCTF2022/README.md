# CrewCTF 2022 Writeup

- Yonjae Lee (yonjae.lee.93@gmail.com)
- Site: <https://crewc.tf> ([CTFTime Info](https://ctftime.org/event/1568/))
- 15 Apr 2022 ~ 15 May 2022

## ez-xor (Crypto)

> its simple xor

The [enc file](./crypto/ez-xor/flag.enc) contains a base64 string.

```text
BRQDER1VHDkeVhQ5BRQfFhIJGw==
```

Given that this problem is about XOR operation, I thought that it would be best to decode this string to hexadecimal format.

```text
>>> binascii.hexlify(base64.b64decode(b'BRQDER1VHDkeVhQ5BRQfFhIJGw=='))
b'051403111d551c391e56143905141f1612091b'
```

I compared the first 5 bytes with the beginning part of the flag format (`crew{`), to see if there is any pattern.

```python
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

'''
M:/mnt/d/GitHub/crewCTF2022/crypto/ez-xor$ python3 exor.py 
b'\x05\x14\x03\x11\x1dU\x1c9\x1eV\x149\x05\x14\x1f\x16\x12\t\x1b'
19
[102, 102, 102, 102, 102]
'''
```

As seen here, every byte of this ciphertext seems to be the result of XOR of a letter from the byte with letter `f` (whose ASCII value is 102). The flag can be obtained by cancelling this XOR operation (i.e., doing the XOR operation with 102 once again).

```python
flag = "".join([chr(x ^ 102) for x in p])
print(flag)
```

**Flag: `crew{3z_x0r_crypto}`**

## Corrupted (Forensics)

> Can you please fix this for me and get the flag

The [file](./forensics/Corrupted.001) is a PNG file with many extra bytes written in front of actual PNG header (`89 50 4e`). Get rid of the extra bytes until the file begins with actual PNG header, and the flag would be [visible](./forensics/Corrupted.png).

**Flag: `crew{34sY_C0rrupt3D_GPT}`**
