import math
import hashlib
import sys
from tqdm import tqdm
import functools

ITERS = int(2e7) # 20000000
ceiling = 10 ** 10000
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfb5885e6c7ed9a3c62b")

# This will overflow the stack, it will need to be significantly optimized in order to get the answer :)
@functools.cache
def m_func(i):
    a = 1 # f(i - 4)
    b = 2 # f(i - 3)
    c = 3 # f(i - 2)
    d = 4 # f(i - 1)
    e = 0 # place for f(i)
    if i < 4:
        return i  + 1

    for i in tqdm(range(4, i + 1)):
        e = ((55692 * a) - (9549 * b) + (301 * c) + (21 * d)) % ceiling
        a = b
        b = c
        c = d
        d = e
    
    return e


# Decrypt the flag
def decrypt_flag(sol):
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = m_func(ITERS) # m_func(20000000) = (55692 * m_func(19999996)) - (9549 * m_func(19999997)) + (302 * m_func(19999998)) + (21 * m_func(19999999))
    decrypt_flag(sol)
