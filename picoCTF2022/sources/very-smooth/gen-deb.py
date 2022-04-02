#!/usr/bin/python

from binascii import hexlify
from gmpy2 import *
import math
import os
import sys

if sys.version_info < (3, 9):
    math.gcd = gcd
    math.lcm = lcm

_DEBUG = False

FLAG  = open('flag.txt').read().strip()
print("FLAG: ", FLAG)
print(FLAG.encode())
FLAG  = mpz(hexlify(FLAG.encode()), 16)
print("mpz hexlify encode FLAG: ", FLAG)
SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
STATE = random_state(SEED)

def get_prime(state, bits):
    # Inputs: state, number of bits.
    # Output: next probable prime number,
    # mpz_urandomb(state, bits) returns random number r such that 0 <= r < (2^bits)
    # and OR(|) operation with (1 << (bits - 1)) assures the result to be (bits)-bit number
    # 2^(bits-1) <= prime < 2^bits 
    return next_prime(mpz_urandomb(state, bits) | (1 << (bits - 1)))

    # if bits = 16
    # mpz_urandomb(state,16) = r,  0 <= r < 65536
    # r | (1 << 15) = r | 32768 = s
    # 32768 <= s < 65536
    # ret = next_prime(32768) = 32771 <= ret < next_prime(65535) = 65537 (e, dropped by next function)
    # if bits = 17
    # mpz_urandomb(state,17) = r,  0 < r < 131072
    # r | (1 << 16) = r | 65536 = s
    # 65536 <= s < 131072
    # ret = next_prime(65536) = 65537 (e, dropped by next function) < ret <= next_prime(131071) = 131101


def get_smooth_prime(state, bits, smoothness=16):
    p = mpz(2) # Initial p is 2
    p_factors = [p] # Initial p factor is 2
    while p.bit_length() < bits - 2 * smoothness: # While p is smaller than 2^(bits-2*smmoothness)
        # in case of main p, 1024 - 2(16) = 1024 - 32 = 992, so while p has 991 or less bits
        # in case of main q, 1024 - 2(17) = 1024 - 34 = 990, so while q has 989 or less bits
        factor = get_prime(state, smoothness) # Keep getting prime factors less than 2^smoothness
        # in case of main p, next_prime(32768) <= factor <= next_prime(65536)
        # in case of main q, next_prime(65536) <= factor <= next_prime(131072)
        p_factors.append(factor) # and add them to the factor list
        p *= factor # multiply p by the latest factor

    bitcnt = (bits - p.bit_length()) // 2
    # returns roughly half of the number of bits to be filled.
    # number of final bits - number of current bits in p,
    # divided by 2 with no remainder
    # Since the previous loop multiplies p until p has 1024 - (2 * smoothness) bits or more,
    # 0 <= bitcnt < smoothness

    while True:
        # Get two primes, 2^(bitcount-1) < prime <= next_prime(2^bitcount) 
        prime1 = get_prime(state, bitcnt)
        prime2 = get_prime(state, bitcnt)
        tmpp = p * prime1 * prime2 # temporary p = p * prime1 * prime2
        # 2^(bits-1) <= tmp-p < 2^bits
        if tmpp.bit_length() < bits: # if tmpp has (bits-1) or less bits, or 1023 or less in main p,q):
            bitcnt += 1 # add another bit and try again
            continue
        if tmpp.bit_length() > bits: # if tmpp has (bits+1) or more bits, or 1025 or more in main p,q):
            bitcnt -= 1 # remove a bit and try again
            continue
        if is_prime(tmpp + 1): # if  2^(bits)<= tmpp < 2^(bits+1) (2^1024 <= main p,q < 2^1025)
                               # and tmpp + 1 is prime:
            p_factors.append(prime1) # add prime1 and prime2 to the factors
            p_factors.append(prime2) # and replace p with tmpp + 1
            p = tmpp + 1             # = (p * prime1 * prime2) + 1
            break # and end the procedure
            # tmpp + 1 will not be 2^1025 because a prime larger than 2 has to be an odd number.
            # the factors are then the factors of tmpp = p - 1, which is lambda(p)

    p_factors.sort()

    return (p, p_factors) #return the final p and factors for Lambda(p)

e = 0x10001 # e = 65537

# Get the right q, right p, and right factors

while True:
    # p is a 1024-bit prime number; p - 1 is next_prime(65536)-smooth 
    p, p_factors = get_smooth_prime(STATE, 1024, 16)
    if len(p_factors) != len(set(p_factors)): # if factors have duplicates, restart
        continue
    # q is a 1024-bit prime number; q - 1 is next_prime(131072)-smooth 
    # Smoothness should be different or some might encounter issues.
    q, q_factors = get_smooth_prime(STATE, 1024, 17)
    if len(q_factors) != len(set(q_factors)): # if factors have duplicates, restart
        continue
    factors = p_factors + q_factors
    if e not in factors: # keep getting a new p, new q until LCM(Lambda(p), Lambda(q)) = LCM(p-1,q-1) is coprime with e
        break

if _DEBUG:
    import sys
    sys.stderr.write(f'p = {p.digits(16)}\n\n')
    sys.stderr.write(f'p_factors = [\n')
    for factor in p_factors:
        sys.stderr.write(f'    {factor.digits(16)},\n')
    sys.stderr.write(f']\n\n')

    sys.stderr.write(f'q = {q.digits(16)}\n\n')
    sys.stderr.write(f'q_factors = [\n')
    for factor in q_factors:
        sys.stderr.write(f'    {factor.digits(16)},\n')
    sys.stderr.write(f']\n\n')

n = p * q 

m = math.lcm(p - 1, q - 1)

d = pow(e, -1, m)

c = pow(FLAG, e, n)

print(f'n = {n.digits(16)}')
print(f'c = {c.digits(16)}')
