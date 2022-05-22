a = [0x65676967,0x34427b6d,0x5f433153,0x616c5f43,0x4175476e,0x525f4567,0x78305f45,0x53414c47,0x00007d53]

s = [int.to_bytes(u, 4, "little").decode() for u in a]

print("".join(s).strip("\x00"))