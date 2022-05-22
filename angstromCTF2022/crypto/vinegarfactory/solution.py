import re
import string
from time import sleep
from pwn import *

context.log_level = "debug"

alpha = string.ascii_lowercase
criteria = re.compile(r"[a-z]{4}\{[a-z_]{9,51}\}[a-z]{4}")

def decrypt(c):
    head = "actf"
    key = ""
    for x in range(4):
        m = alpha[(alpha.index(c[x]) - alpha.index(head[x])) % len(alpha)]
        key += m
    
    ret = ""
    i = 0
    for cm in c:
        if cm in alpha:
            ret += alpha[(alpha.index(cm) - alpha.index(key[i])) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += cm
    return ret

def solve(txt):
    likely = [decrypt(c) for c in criteria.findall(txt)]
    for lk in likely:
        if "}fleg" in lk:
            return lk[:len(lk) - 4]
    
    return "Not solved"
    
flags = []

site = remote("challs.actf.co", 31333)

print(site.recvline())
for i in range(50):
    chal = site.recvline().decode()
    ans = solve(chal)
    flags.append(ans)
    site.sendline(ans.encode())
    sleep(0.5)

print(flags[49])