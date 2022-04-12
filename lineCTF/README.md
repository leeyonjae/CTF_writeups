# Line CTF 2022 writeup

- Yonjae Lee (yonjae.lee.93@gmail.com)
- Site: <https://score.linectf.me/>
- 26 Mar 2022 ~ 27 Mar 2022

## Misc: ecrypt

> New encryption service in Kernel!
>
> nc 34.85.38.218 10002
>
> nc 35.200.2.119 10002

Through netcat, user can access a remote Linux host. The `flag` file is located at the root directory `/`, but only the owner can read it.

```text
$ ls -all
ls -all
total 41
drwxr-xr-x   18 root     root          1024 Mar 22 16:37 .        
drwxr-xr-x   18 root     root          1024 Mar 22 16:37 ..       
drwxr-xr-x    2 root     root          2048 Mar 22 13:44 bin      
drwxr-xr-x    9 root     root          2440 Mar 26 16:32 dev      
-rw-r--r--    1 root     root         15184 Mar 22 13:45 ecrypt.ko
drwxr-xr-x    5 root     root          1024 Mar 22 13:44 etc      
-r--------    1 root     root            39 Mar 22 16:37 flag
drwxr-xr-x    3 root     root          1024 Mar 22 13:44 lib
lrwxrwxrwx    1 root     root             3 Mar 22 12:49 lib64 -> lib
lrwxrwxrwx    1 root     root            11 Mar 22 12:55 linuxrc -> bin/busybox
drwx------    2 root     root         12288 Mar 22 13:44 lost+found
drwxr-xr-x    2 root     root          1024 Mar  8 22:08 media
drwxr-xr-x    2 root     root          1024 Mar  8 22:08 mnt
drwxr-xr-x    2 root     root          1024 Mar  8 22:08 opt
dr-xr-xr-x  103 root     root             0 Mar 26 16:32 proc
drwx------    2 root     root          1024 Mar  8 22:08 root
drwxr-xr-x    3 root     root            80 Mar 26 16:32 run
drwxr-xr-x    2 root     root          1024 Mar 22 13:44 sbin
dr-xr-xr-x   12 root     root             0 Mar 26 16:32 sys
```

I tried to use `sudo` command, but the shell did not even recognize the command. But it did recognize `su` command, even without requiring a password.

```text
/ $ sudo -l
sudo -l
sh: sudo: not found
/ $ su
su
/ # ls
ls
bin         flag        lost+found  proc        sys
dev         lib         media       root        tmp
ecrypt.ko   lib64       mnt         run         usr
etc         linuxrc     opt         sbin        var
/ # chmod 777 flag
chmod 777 flag
/ # cat flag
cat flag
LINECTF{WOW!_powerful_kernel_oor_oow}
```

**Flag: `LINECTF{WOW!_powerful_kernel_oor_oow}`**

## ss-puzzle

> I had stored this FLAG securely in five separate locations. However, three of the shares were lost and one was partially broken. Can you restore flag?

The goal here is to reconstruct the flag from the given parts of ciphertext and encryption scheme.

```text
Share1:
b"%$>*1 '\x15\x00\x00\x00\x00\x00\x00\x00\x00+\x07\x19\x07:\n,/\x02\x14%\x1c\t@H\x13"
Share4:
b'\x1d\x08\x08\x1b-\x1d\x121\x0316\x1e3\x19\x06\x1c\x06\x07\x00\x1b:\x0f1\x1f934)&ug\x06'
```

This is how the author encrypted and stored the flag:

```python
def xor(a:bytes, b:bytes) -> bytes:
    return bytes(i^j for i, j in zip(a, b))

S[0] = FLAG[0:8]
S[1] = FLAG[8:16]
S[2] = FLAG[16:24]
S[3] = FLAG[24:32]

R[0] = FLAG[32:40]
R[1] = FLAG[40:48]
R[2] = FLAG[48:56]
R[3] = FLAG[56:64]

Share[0] = R[0]            + xor(R[1], S[3]) + xor(R[2], S[2]) + xor(R[3],S[1])
Share[1] = xor(R[0], S[0]) + R[1]            + xor(R[2], S[3]) + xor(R[3],S[2])
Share[2] = xor(R[0], S[1]) + xor(R[1], S[0]) + R[2]            + xor(R[3],S[3])
Share[3] = xor(R[0], S[2]) + xor(R[1], S[1]) + xor(R[2], S[0]) + R[3]
Share[4] = xor(R[0], S[3]) + xor(R[1], S[2]) + xor(R[2], S[1]) + xor(R[3],S[0])
```

The factors in Shares 0, 2, and 3 can be derived from factors from Shares 1 and 4, except for `R[0:3]`. However, even after I found all `xor` factors, I still couldn't find the individual values of `S[0:3]` and `R[0:3]`.

So I tried to retrieve the flag by assuming the first part of the flag, `S[0]`, as `LINECTF{`. I wrote a [script](solutions/ss-puzzle.py) to do all the operations.

```text
M:/mnt/d/GitHub/lineCTF/solutions$ python3 ss-puzzle.py 
FLAG: LINECTF{Yeah_lnown_plaintext_is_important_in_xor_basec_puzzle!!}
```

For some reason, the resulting flag had a couple of bytes that did not match the actual flag below.

**Flag: `LINECTF{Yeah_known_plaintext_is_important_in_xor_based_puzzle!!}`**
