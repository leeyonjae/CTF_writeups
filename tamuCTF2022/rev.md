# TAMU CTF - Reverse Engineering

## Covfefe

> This one might require a nice hot cup of Java to get through.

The source code of [the program](rev/covfefe/Covfefe.class) can be obtained via tools like JD-gui.

```java
public class Covfefe {
  public static void main(String[] paramArrayOfString) {
    byte b1 = 35;
    int[] arrayOfInt = new int[b1];
    byte b2;
    for (b2 = 0; b2 < b1; b2++)
      arrayOfInt[b2] = 0; 
    arrayOfInt[0] = 103;
    arrayOfInt[1] = arrayOfInt[0] + 2;
    arrayOfInt[2] = arrayOfInt[0];
    for (b2 = 3; b2 < 8; b2++) {
      switch (b2) {
        case 3:
          arrayOfInt[b2] = 101;
          break;
        case 4:
          arrayOfInt[6] = 99;
          break;
        case 5:
          arrayOfInt[5] = 123;
          break;
        case 6:
          arrayOfInt[b2 + 1] = 48;
          break;
        case 7:
          arrayOfInt[4] = 109;
          break;
      } 
    } 
    arrayOfInt[8] = 102;
    arrayOfInt[9] = arrayOfInt[8];
    arrayOfInt[28] = arrayOfInt[7];
    arrayOfInt[25] = arrayOfInt[7];
    arrayOfInt[24] = arrayOfInt[7];
    arrayOfInt[10] = 51;
    arrayOfInt[11] = arrayOfInt[10] + 12 - 4 - 4 - 4;
    arrayOfInt[27] = arrayOfInt[0] - (int)Math.pow(2.0D, 3.0D);
    arrayOfInt[22] = arrayOfInt[0] - (int)Math.pow(2.0D, 3.0D);
    arrayOfInt[15] = arrayOfInt[0] - (int)Math.pow(2.0D, 3.0D);
    arrayOfInt[12] = arrayOfInt[0] - (int)Math.pow(2.0D, 3.0D);
    arrayOfInt[13] = 49;
    arrayOfInt[14] = 115;
    for (b2 = 16; b2 < 22; b2++) {
      switch (b2) {
        case 16:
          arrayOfInt[b2 + 1] = 108;
          break;
        case 17:
          arrayOfInt[b2 - 1] = 52;
          break;
        case 18:
          arrayOfInt[b2 + 1] = 52;
          break;
        case 19:
          arrayOfInt[b2 - 1] = 119;
          break;
        case 20:
          arrayOfInt[b2 + 1] = 115;
          break;
        case 21:
          arrayOfInt[b2 - 1] = 121;
          break;
      } 
    } 
    arrayOfInt[23] = 103;
    arrayOfInt[26] = arrayOfInt[23] - 3;
    arrayOfInt[29] = arrayOfInt[26] + 20;
    arrayOfInt[30] = arrayOfInt[29] % 53 + 53;
    arrayOfInt[31] = arrayOfInt[0] - 18;
    arrayOfInt[32] = 80;
    arrayOfInt[33] = 83;
    arrayOfInt[b1 - 1] = (int)Math.pow(5.0D, 3.0D);
  }
}

```

The code creates an integer array with 35 items and performs various mathematical operations on each item. It is likely that the numbers in the array will correspond to some of the letters in the ASCII table. 

Below is the script that I wrote to print out the said corresponding letters.

```python
b1 = 35

arrayOfInt = [0] * b1

arrayOfInt[0] = 103
arrayOfInt[1] = arrayOfInt[0] + 2
arrayOfInt[2] = arrayOfInt[0]
arrayOfInt[3] = 101
arrayOfInt[6] = 99
arrayOfInt[5] = 123
arrayOfInt[7] = 48
arrayOfInt[4] = 109
arrayOfInt[8] = 102
arrayOfInt[9] = arrayOfInt[8]
arrayOfInt[28] = arrayOfInt[7]
arrayOfInt[25] = arrayOfInt[7]
arrayOfInt[24] = arrayOfInt[7]
arrayOfInt[10] = 51
arrayOfInt[11] = arrayOfInt[10] + 12 - 4 - 4 - 4
arrayOfInt[27] = arrayOfInt[0] - pow(2, 3)
arrayOfInt[22] = arrayOfInt[0] - pow(2, 3)
arrayOfInt[15] = arrayOfInt[0] - pow(2, 3)
arrayOfInt[12] = arrayOfInt[0] - pow(2, 3)
arrayOfInt[13] = 49
arrayOfInt[14] = 115

arrayOfInt[17] = 108
arrayOfInt[16] = 52
arrayOfInt[19] = 52
arrayOfInt[18] = 119
arrayOfInt[21] = 115
arrayOfInt[20] = 121

arrayOfInt[23] = 103
arrayOfInt[26] = arrayOfInt[23] - 3
arrayOfInt[29] = arrayOfInt[26] + 20
arrayOfInt[30] = arrayOfInt[29] % 53 + 53
arrayOfInt[31] = arrayOfInt[0] - 18
arrayOfInt[32] = 80
arrayOfInt[33] = 83
arrayOfInt[b1 - 1] = pow(5, 3)

s = "".join([chr(i) for i in arrayOfInt])

print(s)
```

Executing this script yields the flag.

```text
PS D:\GitHub\tamuCTF2022> & C:/Python310/python.exe d:/GitHub/tamuCTF2022/rev/covfefe/covfefe.py
gigem{c0ff33_1s_4lw4ys_g00d_0xCUPS}
```

**Flag: `gigem{c0ff33_1s_4lw4ys_g00d_0xCUPS}`**

## REdo 1

> Just a basic reverse engineering challenge. Nothing special. See what you can do.

The [source code](rev/redo1/code.c) contains an `int` array and a loop to compare the arguments with the supposed flag.

```c++
#include <stdio.h>
#include <string.h>

#define STR_LEN 34

#define EXIT printf("Sorry that's not the flag\n"); return 1;
#define SUCCESS printf("THAT'S THE FLAG!\n"); return 0;
#define PARAMS printf("Usage: ./code <flag>\n"); return 1;
#define POINTER char* flag = (char*)(&a);

int main(int argc, char** argv) 
{
    int a[] = {0x65676967,0x00000000,0x34427b6d,0x5f433153,0x616c5f43,0x00000000,0x4175476e,0x525f4567,0x00000000,0x78305f45,0x53414c47,0x00007d53};

    if(argc != 2){ PARAMS }
    if(strlen(argv[1]) != STR_LEN){ EXIT }

    POINTER

    for(int i = 0; i < STR_LEN; i++)
    {
        int idx = i;
        if(i >= 4 && i <= 15){ idx += 4; }
        if(i >= 16 && i <= 23){ idx += 8; }
        if(i > 23){ idx += 12; }

        if(argv[1][i] != flag[idx]){ EXIT }
    }

    SUCCESS
}

```

The line `#define POINTER char* flag = (char*)(&a);` indicates that the words stored in `a[]` are in fact parts of the flag. The flag is stored in little endian, and we get the flag by eliminating all-null words(`0x00000000`) and converting the rest to string.

```python
a = [0x65676967,0x34427b6d,0x5f433153,0x616c5f43,0x4175476e,0x525f4567,0x78305f45,0x53414c47,0x00007d53]

s = [int.to_bytes(u, 4, "little").decode() for u in a]

print("".join(s).strip("\x00"))
```

Executing this script yields the flag.

```text
/mnt/d/GitHub/tamuCTF2022/rev/redo1$ python3 solver.py 
gigem{B4S1C_C_lanGuAgE_RE_0xGLASS}
```

**Flag: `gigem{B4S1C_C_lanGuAgE_RE_0xGLASS}`**
