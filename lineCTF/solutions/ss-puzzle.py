#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ss-puzzle solution

# 64 bytes

def xor(a:bytes, b:bytes) -> bytes:
    return bytes(i^j for i, j in zip(a, b))


# Share[1] = xor(R[0], S[0]) + R[1] (broken)   + xor(R[2], S[3]) + xor(R[3],S[2])
#               8 bytes             8 bytes             8 bytes       8 bytes

share1 = b""
for l1 in open("../sources/ss-puzzle/Share1").read(64):
    share1 += l1.encode()

print(share1)
s11 = share1[0:8]
s12 = share1[8:16]
s13 = share1[16:24]
s14 = share1[24:32]

# Share[4] = xor(R[0], S[3]) + xor(R[1], S[2]) + xor(R[2], S[1]) + xor(R[3],S[0])
#               8 bytes             8 bytes             8 bytes       8 bytes

share4 = b""
for l2 in open("../sources/ss-puzzle/Share4").read(64):
    share4 += l2.encode()

print(share4)
s41 = share4[0:8]
s42 = share4[8:16]
s43 = share4[16:24]
s44 = share4[24:32]


'''
Share[0] = R[0]            + xor(R[1], S[3]) + xor(R[2], S[2]) + xor(R[3],S[1])
           s01               s02               s03               s04
Share[1] = xor(R[0], S[0]) + R[1]            + xor(R[2], S[3]) + xor(R[3],S[2])
           s11               s12               s13               s14
Share[2] = xor(R[0], S[1]) + xor(R[1], S[0]) + R[2]            + xor(R[3],S[3])
           s21               s22               s23               s24
Share[3] = xor(R[0], S[2]) + xor(R[1], S[1]) + xor(R[2], S[0]) + R[3]
           s31               s32               s33               s34
Share[4] = xor(R[0], S[3]) + xor(R[1], S[2]) + xor(R[2], S[1]) + xor(R[3],S[0])
           s41               s42               s43               s34
'''

# r2^s3 ^ r2^s1  ^  r0^s3 = s3^s1 ^ r0^s3 = r0^s1
s21 = xor(xor(s13, s43), s41)

# r3^s2 ^ r3^s0  ^  r1^s2 = s2^s0 ^ r1^s2 = r1^s0
s22 = xor(xor(s14, s44), s42)

# r0^s0 ^ r0^s3  ^  r3^s0 = s0^s3 ^ r3^s0 = r3^s3
s24 = xor(xor(s11, s41), s44)

# r0^s0 ^ r1^s0  ^  r1^s2 = r0^r1 ^ r1^s2 = r0^s2
s31 = xor(xor(s11, s22), s42)

# r2^s3 ^ r0^s3  ^  r0^s2 = r0^r2 ^ r0^s2 = r2^s2
s03 = xor(xor(s13, s41), s31)

# r2^s2 ^ r2^s3  ^  r1^s2 = s2^s3 ^ r1^s2 = r1^s3
s02 = xor(xor(s03, s13), s41)

# r2^s2 ^ r3^s2  ^  r2^s1 , r2^r3 ^ r2^s1 = r3^s1
s04 = xor(xor(s03, s13), s43)

# r0^s0 ^ r0^s1  ^  r1^s0 = s0^s1 ^ r1^s0 = r1^s1
s32 = xor(xor(s11, s21), s22)

# r1^s0 ^ r1^s1  ^  r2^s1 = s0^s1 ^ r2^s1 = r2^s0
s33 = xor(xor(s22, s32), s43)


share3 = s31 + s32 + s33

print(bin(int.from_bytes(s21, 'big')))
print(bin(int.from_bytes(share3[:8],'big')))

#  assume s[0] = b'LINECTF{'



s0 = b'LINECTF{'
r0 = xor(s11, s0)

s1 = xor(s21, r0)

s2 = xor(s31, r0)

s3 = xor(s41, r0)
r1 = xor(s22, s0)

r2 = xor(s03, s2)

r3 = xor(s44, s0)

print("s1:", s1.decode())
print("r2:", r2.decode())

FLAG = (s0 + s1 + s2 + s3 + r0 + r1 + r2 + r3)

print("FLAG:", FLAG.decode('utf-8'))