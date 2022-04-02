#!/usr/bin/python
# NSA Backdoor solution

from binascii import hexlify
from gmpy2 import *
from tqdm import tqdm
import math
import os
import sys

if sys.version_info < (3, 9):
    math.gcd = gcd
    math.lcm = lcm

# n = p * q
n = mpz("d63c7cb032ae4d3a43ecec4999cfa8f8b49aa9c14374e60f3beeb437233e44f988a73101f9b20ffb56454350b1c9032c136142220ded059876ccfde992551db46c27f122cacdd38c86acb844032f8600515aa6ccb7a1d1ac62d04b51b752476d2d6ee9f22d0f933bebdd833a71fd30510479fcc7ba0afb1d4b0a1622cdc2a48341010dffdcfc8d9af45959fb30b692dc2c9e181ac6bcd6a701326e3707fb19b7f9dfe1c522c68f9b0d229d384be1e1c58f72f8df60ca5172a341a7ee81428a064beedd6af7b89cc6079f2b6d3717f0d29330f0a70acca05bf67ab60c2e5cb0b86bfca2c9b8d50d79d24371432a1efb243f3c5f15b377ccc51f6e69bfbf5ecc61", 16)

# c = 3 ^ (flag) mod n; g = 3
c = mpz("51099773fd2aafd5f84dfe649acbb3558797f58bdc643ac6ee6f0a6fa30031767966316201c36be69241d9d05d0bd181ced13809f57b0c0594f6b29ac74bc7906dae70a2808799feddc71cf5b28401100e5e7e0324b9d8b56e540c725fa4ef87b9e8d0f901630da5f7f181f6d5b4cdc00d5f5c3457674abcb0d0c173f381b92bdfb143c595f024b98b9900410d502c87dfc1633796d640cb5f780fa4b6f0414fb51e34700d9096caf07b36f4dcd3bb5a2d126f60d3a802959d6fadf18f4970756f3099e14fa6386513fb8e6cdda80fdc1c32a10f6cdb197857caf1d7abf3812e3d9dcda106fa87bac382d3e6fc216c55da02a0c45a482550acb2f58bea2cfa03", 16)

def pollard(n):
    a = mpz(13)
    i = mpz(2)
    d = mpz(0)
    while True:
        a = pow(a, i, n)
        d = mpz(math.gcd(a - mpz(1), n))
        if d > mpz(1) and n > d:
            break
        else:
            i += mpz(1)
    
    return d

#p = pollard(n)
#q = mpz(n // p)

p = mpz(165904771154636133744258537155010957898841320976199637310247946276091086685264203988382040434355973963755682908150999129715814054881305005279715109357952947956732031939179558028421896612221813299929875548130332311862653487519381871784418328675201518221252865046296276946334529508065441554563296058286139050519)
q = mpz(n // p)

def ph(n, g, h): # Regular Pohlig-Hellman
    # Inputs 
    # n = prime modulus
    # g = generator
    # h = element
    # Output
    # x, the exponent such that g ^ x (mod n) = h (mod n)
    z = n - 1
    prime = next_prime(1)
    list_pi = []
    list_ei = []
    prime_order = -1 # It will increase to 0 when adding first prime to x

    # Collect Primes
    while is_prime(z) == False:
        if z % prime == mpz(0): # Add prime it it is a factor of p - 1
            z = z // prime # divide p - 1 with prime
            if prime not in list_pi: # if it is a new prime
                list_pi.append(prime) # add it to the list of primes
                list_ei.append(1) # start with exponent 1
                prime_order += 1
            else: # if it is repeat of previous prime
                list_ei[prime_order] += 1 # increase the exponent
        else:
            prime = next_prime(prime)

    if z not in list_pi:
        list_pi.append(z)
        list_ei.append(1)
    else:
        list_ei[len(list_ei) - 1] += 1

    #print("DEBUG: len(list_pi):", len(list_pi))

    xxp = []
    for i in range(len(list_pi)):
        xxp.append((list_pi[i], list_ei[i]))
    
    
    #print("DEBUG: len(xxp):", len(xxp))

    small_xs = []

    for j in range(len(xxp)):
        # xj = coef0 + coef1*pj + coef2*pj^2 + coef3*pj^3 + ...
        # xj (mod pj^ej) = x (mod pj^ej)
        xj = mpz(0)

        pj, ej = xxp[j] # pj = base, ej = exponent = num of coefficients (c0, c1, .. c(ej-1))
        for coef in range(ej):
            # Exponent = (n - 1) / pj^(coef + 1)
            corp = (n - 1) // pow(pj, coef + 1)
            corpp = pow(pj, coef)
            if xj == mpz(0):
                cmp = h 
            else:
                cmp = (h * pow(g, (xj * -1), n)) % n
            
            for possible_coef in range(int(pj)): # 0 <= coefj < pj
                #if pj > 100 and possible_coef > 100 and possible_coef % (pj // 100) == 0:
                    #print(f"DEBUG: possible coef {math.floor((possible_coef / pj) * 100)} %...")
                if pow(cmp, corp, n) == pow(g, corpp * corp * possible_coef, n):
                    xj = xj + (possible_coef * corpp)
                    break
            
        small_xs.append((xj, pow(pj, ej)))
        #print(f"DEBUG: small_xs: {len(small_xs)} / {len(xxp)}")

    # Chinese Remainder Theorem
    x = mpz(0)
    for small_x in small_xs:
        print(small_x)
        xmod, modulus = small_x
        mx = (n - 1) // modulus
        yx = pow(mx, -1, modulus)
        x = x + (xmod * mx * yx)
    
    return x % (n - 1)

#ph_p = ph(p, mpz(3), c)
ph_p = mpz(82952385577318066872129268577505478949420660488099818655123973138045543342632101994191020217177986981877841454075499564857907027440652502639857554678976473978366015969589779014210948306110906649964937774065166155931326743759690935892209164337600759110626432523148138511418975082806074640955350929047360880008)
#ph_q = ph(q, mpz(3), c)
ph_q = mpz(81507072874510483263681433236692584859425860808049790446482019230437229150114783298525563565918863882838289236371915864243595099942328832381552731374659527893857559879830435122625569833466947217108606505061833950888158569865073607919009978301841512083415120347419757581802483299551189448238855482315266111648)



print("======================= Pohlig-Hellman Finished =========================")
print("PH(p):", ph_p)
print("PH(q):", ph_q)
ph_q2 = ph_q % ((q - 1)//2)


'''
n = p * q
x mod p - 1 = ph(p, 3, c) mod p - 1 = p1 * p2 * ... * pk * 2
x mod q - 1 = ph(q, 3, c) mod q - 1 = q1 * q2 * ... * ql * 2
phi_n = (p - 1)(q - 1)
y1 = phi_n / (p - 1) = q - 1
y2 = phi_n / (q - 1) = p - 1
z1 = y1^-1 mod (p - 1)
z2 = y2^-1 mod (q - 1)
x = ph_p * (q - 1) * z1 + ph_q * (p - 1) * z2
'''
n1 = p - 1
n2 = (q - 1) // 2
y1 = (q - 1) // 2
y2 = p - 1
z1 = pow(y1, -1, n1)
z2 = pow(y2, -1, n2)
x = ((ph_p * y1 * z1) + (ph_q2 * y2 * z2)) % ((n1 * n2) // 2)

flag = bytes.fromhex(str(x.digits(16))).decode()
print("Flag:", flag)