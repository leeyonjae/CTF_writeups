# Reverse Engineering

## file-run1 (100 pts)

> A program has been provided to you, what happens if you try to run it on the command line?
>
> Download the program [here](sources/file-run).

I ran the program on the shell and

```bash
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ ./file-run 
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}
```

**Flag: `picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}`**

## file-run2 (100 pts)

> Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?
> Download the program [here](sources/file-run2).

This program needed an argument to operate. I entered `Hello!` as instructed, and it printed the flag.

```bash
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ ./file-run2
Run this file with only one argument.
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ ./file-run2 Hello!
The flag is: picoCTF{F1r57_4rgum3n7_be0714da}
```

**Flag: `picoCTF{F1r57_4rgum3n7_be0714da}`**

## GDB Test Drive (100 pts)

> Can you get the flag?
>
> Download this [binary](sources/gdbme).
>
> Here's the test drive instructions:
> 
> ```bash
> $ chmod +x gdbme
> $ gdb gdbme
> (gdb) layout asm
> (gdb) break *(main+99)
> (gdb) run
> (gdb) jump *(main+104)
> ```

```text
Breakpoint 1, 0x000000000800132a in main ()
(gdb) jump *(main+104)
Continuing at 0x800132f.
[Inferior 1 (process 1150) exited normally]
```

I followed the test drive instruction and got the flag.

**Flag: `picoCTF{d3bugg3r_dr1v3_197c378a}`**

## patchme.py (100 pts)

> Can you get the flag?
>
> Run [this Python program](sources/patchme-py/patchme.flag.py) in the same directory as this encrypted [flag](sources/patchme-py/flag.txt.enc).

The Python program has a function that checks for password. Wrong password will prevent decryption.

```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")

```

The correct password is `ak98-=90adfjhgj321sleuth9000`.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/patchme-py$ python3 patchme.flag.py 
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
```

**Flag: `picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}`**

## Safe Opener (100 pts)

> Can you open this safe?
>
> I forgot the key to my safe but this [program](sources/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
>
> Put the password you recover into the picoCTF flag format like:
>
> `picoCTF{password}`

The program is written in Java. The `main` function receives user input as password, encodes it in Base64, and passes it to the authentication function which compares it to the hard-coded Base64 password.

```java
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              
            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }

    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
```

I used Base64 decoder to decode the hard-coded password `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`. The result was `pl3as3_l3t_m3_1nt0_th3_saf3`.

**Flag: `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`**

## unpackme.py (100 pts)

> Can you get the flag?
>
> Reverse engineer this [Python program](sources/unpackme.flag.py).

The Python program asks for a password and prints if it is correct. The below is the code:

```python
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABiMD04m0Z6CohVV7ozdwHqtgc2__CuAFGG8rWhZBTL0lhfzp-mhu9LYNMnMQMGO-7tEwy3DJ2Y8yjogvzyojFETwN9YEIPXTnO9F1QnkPypWTgjISGve4gcSerJMs694oKcIdKHuVaSxOg1MMNs5k9iPaBIPU7xOKQqCyhnf_f4yUvLdMcer38BqRptocJNvKlyWN8h7ikoWL0zlssxd8OJyPujMz78HZaefvUouvq6LDtPVqRBJFPgSJYf1nHpHKFa1O0zJ6UpTe6ba3PPAxCVXutNg=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```

The interesting part was that the crux of this program was encrypted with Fernet symmetric encryption, with the key being `correctstaplecorrectstaplecorrec`. Then it would decrypt the code with the key and execute it.

I added another line between the last line and the second-to-last line:

```python
print(plain)
```

When the program was run, it now printed the decrypted code.

```powershell
D:\GitHub\picoCTF2022> & C:/Python310/python.exe d:/GitHub/picoCTF2022/sources/unpackme.flag.py
b"\npw = input('What\\'s the password? ')\n\nif pw == 'batteryhorse':\n  print('picoCTF{175_chr157m45_5274ff21}')\nelse:\n  print('That password is incorrect.')\n\n"
What's the password? 
```

The code had a pre-coded password, which was `batteryhorse`. When I entered it, the program printed the flag.

**Flag: `picoCTF{175_chr157m45_5274ff21}`**

## bloat.py (200 pts)

> Can you get the flag?
>
> Run this [Python program](sources/bloat-py/bloat.flag.py) in the same directory as this [encrypted flag](sources/bloat-py/flag.txt.enc).

The Python program asks for the password and check if it is correct. The source code has functions and variables, but they do not have meaningful names, and even their contents refers to various parts of the charset at the beginning. It is hard to understand the code at first look.

```python
import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def arg133(arg432):
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
  else:
    print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
a[81]+a[68]+a[66]+a[83])
    sys.exit(0)
    return False
def arg111(arg444):
  return arg122(arg444.decode(), a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+\
a[75]+a[72]+a[78]+a[77])
def arg232():
  return input(a[47]+a[75]+a[68]+a[64]+a[82]+a[68]+a[94]+a[68]+a[77]+a[83]+\
a[68]+a[81]+a[94]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+\
a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+a[81]+a[67]+a[94]+\
a[69]+a[78]+a[81]+a[94]+a[69]+a[75]+a[64]+a[70]+a[25]+a[94])
def arg132():
  return open('flag.txt.enc', 'rb').read()
def arg112():
  print(a[54]+a[68]+a[75]+a[66]+a[78]+a[76]+a[68]+a[94]+a[65]+a[64]+a[66]+\
a[74]+a[13]+a[13]+a[13]+a[94]+a[88]+a[78]+a[84]+a[81]+a[94]+a[69]+\
a[75]+a[64]+a[70]+a[11]+a[94]+a[84]+a[82]+a[68]+a[81]+a[25])
def arg122(arg432, arg423):
    arg433 = arg423
    i = 0
    while len(arg433) < len(arg432):
        arg433 = arg433 + arg423[i]
        i = (i + 1) % len(arg423)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(arg432,arg433)])
arg444 = arg132()
arg432 = arg232()
arg133(arg432)
arg112()
arg423 = arg111(arg444)
print(arg423)
sys.exit(0)
```

The first function (`arg133`) checks if the input matches `a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]`, which translates to `happychance`.

I was curious if `happychance` was the password. So I tested if that was the case, and got the flag.

```text
I52HE8M:/mnt/d/GitHub/picoCTF2022/sources/bloat-py$ python3 bloat.flag.py 
Please enter correct password for flag: happychance
Welcome back... your flag, user:
picoCTF{d30bfu5c4710n_f7w_b8062eec}
```

I also deobfusticated the code [here](solutions/bloat.py).

**Flag: `picoCTF{d30bfu5c4710n_f7w_b8062eec}`**

## Fresh Java (200 pts)

> Can you get the flag?
>
> Reverse engineer this [Java program](sources/fresh-java/KeygenMe.class).

The given program was a Java class file, which cannot be read easily by text editor.

I used [JD-GUI](http://java-decompiler.github.io/) to extract [the source code](solutions/fresh-java.java) from the class file.

This program has a series of conditionals that asks if a character at a specific location of the input is a certain character. The check starts from the last character to the first character (backwards). A part of the code is shown below:

```java
    if (str.charAt(33) != '}') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(32) != '9') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(31) != '8') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(30) != 'c') {
      System.out.println("Invalid key");
      return;
```

I got the flag by gathering all of the valid letters from 1st to 34th. 

**Flag: `picoCTF{700l1ng_r3qu1r3d_738cac89}`**

## Bbbbloat (300 pts)

> Can you get the flag?
>
> Reverse engineer this [binary](sources/bbbbloat/bbbbloat).

The binary asks the user to guess its favorite number.

I opened the binary with [IDA](https://hex-rays.com/ida-free/). When I looked at the `main` function, I found the part where the wrong answer message shows up:

```text
loc_1583:
lea     rdi, s          ; "Sorry, that's not it!"
call    _puts
```

The `loc_1583` code is called by this part of the `main`.

```text
cmp     eax, 86187h
jnz     loc_1583
```

I guessed that the input value is compared to `86187h` and the error message occurs when they do not match.

`86187h` meant that the number was hexadecimal; in decimal, `86187(16)` was `549255`. I checked if this was the favorite number:

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/bbbbloat$ ./bbbbloat 
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_36dd316a}
```

**Flag: `picoCTF{cu7_7h3_bl047_36dd316a}`**

## unpackme (300 pts)

> Can you get the flag?
>
> Reverse engineer this [binary](sources/unpackme/unpackme-upx).

The binary is a 64-bit binary. When run, it asks for its favorite number. I tried to see the source with `objdump` but it did not return any code. But I was able to open this with IDA. But even IDA did not provide meaningful information.

It turned out that the file name had a crucial hint: it was compressed using [UPX](https://upx.github.io/). I downloaded the UPX program and decompressed the binary.

```powershell
PS C:\Users\USER\Documents\upx-3.96-win64> C:\Users\USER\Documents\upx-3.96-win64\upx.exe -d D:\GitHub\picoCTF2022\sources\unpackme\unpackme-upx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96w       Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   1002408 <-    379108   37.82%   linux/amd64   unpackme-upx

Unpacked 1 file.
```

I opened the unpacked binary with IDA again and found the `main` function.

```text
; int __cdecl main(int argc, const char **argv, const char **envp)
public main
main proc near

var_50= qword ptr -50h
var_44= dword ptr -44h
var_3C= dword ptr -3Ch
var_38= qword ptr -38h
var_30= qword ptr -30h
var_28= qword ptr -28h
var_20= qword ptr -20h
var_18= dword ptr -18h
var_14= word ptr -14h
var_8= qword ptr -8

endbr64
push    rbp
mov     rbp, rsp
sub     rsp, 50h
mov     [rbp+var_44], edi
mov     [rbp+var_50], rsi
mov     rax, fs:28h
mov     [rbp+var_8], rax
xor     eax, eax
mov     rax, 4C75257240343A41h
mov     rdx, 30623E306B6D4146h
mov     [rbp+var_30], rax
mov     [rbp+var_28], rdx
mov     rax, 3532666630486637h
mov     [rbp+var_20], rax
mov     [rbp+var_18], 36665F60h
mov     [rbp+var_14], 4Eh ; 'N'
lea     rdi, aWhatSMyFavorit ; "What's my favorite number? "
mov     eax, 0
call    printf
lea     rax, [rbp+var_3C]
mov     rsi, rax
lea     rdi, aD         ; "%d"
mov     eax, 0
call    __isoc99_scanf
mov     eax, [rbp+var_3C]
cmp     eax, 0B83CBh
jnz     short loc_401F42
```

The magic number was `0xB83CB`, which was `754635` in decimal.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/unpackme$ ./unpackme-upx 
What's my favorite number? 754635
picoCTF{up><_m3_f7w_77ad107e}
```

**Flag: `picoCTF{up><_m3_f7w_77ad107e}`**

## Keygenme (400 pts)

> Can you get the flag?
>
> Reverse engineer this [binary](sources/keygenme/keygenme).

The binary asks for a license key that I need to find.

When I disassembled it, the program did not contain a `main` function. When I opened it with IDA, it identified the de facto `main` at `0x0148b`.

I decompiled the `main` part and the subroutine called after the program accepts the input from the `stdin`. 

```cpp
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  char v3; // al
  char s[40]; // [rsp+10h] [rbp-30h] BYREF
  unsigned __int64 v6; // [rsp+38h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  printf("Enter your license key: ");
  fgets(s, 37, stdin);
  ((void (__fastcall *)())((char *)&sub_1208 + 1))();
  if ( v3 )
    puts("That key is valid.");
  else
    puts("That key is invalid.");
  return 0LL;
}

__int64 __fastcall sub_120A(const char *a1) // sub_1208 itself ends in failure; make a new function at address 120A to decompile
{
  __int64 v1; // rbp
  size_t v2; // rax
  size_t v3; // rax
  int v5; // [rsp-D0h] [rbp-D0h]
  int v6; // [rsp-D0h] [rbp-D0h]
  int i; // [rsp-CCh] [rbp-CCh]
  int j; // [rsp-C8h] [rbp-C8h]
  int k; // [rsp-C4h] [rbp-C4h]
  int m; // [rsp-C0h] [rbp-C0h]
  __int16 v11; // [rsp-BAh] [rbp-BAh] BYREF
  _BYTE v12[16]; // [rsp-B8h] [rbp-B8h] BYREF
  _BYTE v13[16]; // [rsp-A8h] [rbp-A8h] BYREF
  char flag[61]; // [rsp-98h] [rbp-98h] BYREF // original name is v14
  char v15; // [rsp-5Bh] [rbp-5Bh]
  _BYTE v16[72]; // [rsp-58h] [rbp-58h] BYREF
  unsigned __int64 v17; // [rsp-10h] [rbp-10h]
  __int64 v18; // [rsp-8h] [rbp-8h]

  v18 = v1;
  v17 = __readfsqword(0x28u);
  strcpy(flag, "picoCTF{br1ng_y0ur_0wn_k3y_");
  v11 = 125;
  v2 = strlen(flag);
  MD5(flag, v2, v12);
  v3 = strlen((const char *)&v11);
  MD5(&v11, v3, v13);
  v5 = 0;
  for ( i = 0; i <= 15; ++i )
  {
    sprintf(&flag[v5 + 32], "%02x", (unsigned __int8)v12[i]);
    v5 += 2;
  }
  v6 = 0;
  for ( j = 0; j <= 15; ++j )
  {
    sprintf(&v16[v6], "%02x", (unsigned __int8)v13[j]);
    v6 += 2;
  }
  for ( k = 0; k <= 26; ++k )
    v16[k + 32] = flag[k];
  v16[59] = flag[45];
  v16[60] = flag[50];
  v16[61] = v15;
  v16[62] = flag[33];
  v16[63] = flag[46];
  v16[64] = flag[56];
  v16[65] = flag[58];
  v16[66] = v15;
  v16[67] = v11;
  if ( strlen(a1) != 36 )
    return 0LL;
  for ( m = 0; m <= 35; ++m )
  {
    if ( a1[m] != v16[m + 32] )
      return 0LL;
  }
  return 1LL;
}
```

From these functions, I guessed that the key to yield the input `"That key is valid."` is the flag. So I wrote the [script](solutions/keygenme.py) where I replicated the second routine's effort to assemble the key. 

At the end of the step, the key was likely to have a form of `picoCTF{br1ng_y0ur_0wn_k3y_19[?]36cd[?]}`. There was one unknown variable (`v15`) that I could not solve. But it was likely to be one within `[0-9a-zA-Z]`. So I created a loop to brute-force this, and got the flag.

**Flag: `picoCTF{br1ng_y0ur_0wn_k3y_19836cd8}`**
