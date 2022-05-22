# TAMU CTF - Forensics

## Plain

> Someone logged into my computer and stole my flag. Can you get it back for me?

The attacker used telnet to log in and browse the flag.

```text
Z2lnZW17ZDBudF91czNfdDNsbmV0X2V2M3J9Cg==
```

The flag is encoded in base64. Decode it to find the flag.

```text
/mnt/d/GitHub/tamuCTF2022$ python3
Python 3.9.10 | packaged by conda-forge | (main, Feb  1 2022, 21:24:11) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64
>>> base64.b64decode('Z2lnZW17ZDBudF91czNfdDNsbmV0X2V2M3J9Cg==')
b'gigem{d0nt_us3_t3lnet_ev3r}\n'
```

**Flag: `gigem{d0nt_us3_t3lnet_ev3r}`**

## What's the Difference

> I made a mistake while making a writeup for a challenge from MetaCTF 2021. Can you find it?

We are given a `README.md` file and a `.git` folder. The latter allows us to see the git commit history and the changes made to the former. One of the commits, with summary `whoops! wrong flag`, shows the flag.

**Flag: `gigem{b3_car3ful_b3for3_y0u_c0mmit}`**
