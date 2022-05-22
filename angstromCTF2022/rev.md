# AngstromCTF - Reverse Engineering

## baby3 (40 pts)

> [This program](rev/baby3) doesn't do anything.

Due to the GLIBC version problem I could not run the program. But the fragments of the flag are visible when opened with disassembler.

```text
push    rbp
mov     rbp, rsp
sub     rsp, 40h
mov     rax, fs:28h
mov     [rbp+var_8], rax
xor     eax, eax
mov     rax, 'hme{ftca'
mov     rdx, 'ezemdiap'
mov     [rbp+var_40], rax
mov     [rbp+var_38], rdx
mov     rax, 'rallodor'
mov     rdx, 'tekamots'
mov     [rbp+var_30], rax
mov     [rbp+var_28], rdx
mov     rax, 'llahcsih'
mov     rdx, 'oma_egne'
mov     [rbp+var_20], rax
mov     [rbp+var_18], rdx
mov     [rbp+var_10], '}sug'
mov     [rbp+var_C], 0
```

The program is a 64-bit program and its endianness is little endian. Therefore, reverse every 8-letter blocks of the string (4-letter block for the last part) to get the flag.

**Flag: `actf{emhpaidmezerodollarstomakethischallenge_amogus}`**

## Number Game (70 pts)

> Step right up and enter clam's [number game](rev/number-game)! Winners get one (1) free flag!!!
>
> Connect to it at `nc challs.actf.co 31334`.

This program asks user to enter a number and see if it is what the program expected.

```text
8M:/mnt/d/GitHub/angstromCTF2022/rev$ ./number-game 
Welcome to clam's number game!
Step right up and guess your first number: 236
Sorry but you didn't win :(
```

When you disassemble the program, there are some lines that compare user input to a certain number.

```text
0x0000000000001249 <+0>:     push   rbp
   0x000000000000124a <+1>:     mov    rbp,rsp
   0x000000000000124d <+4>:     sub    rsp,0x50
   0x0000000000001251 <+8>:     lea    rdi,[rip+0xe10]        # 0x2068
   0x0000000000001258 <+15>:    call   0x1030 <puts@plt>
   0x000000000000125d <+20>:    lea    rdi,[rip+0xe24]        # 0x2088
   0x0000000000001264 <+27>:    mov    eax,0x0
   0x0000000000001269 <+32>:    call   0x1040 <printf@plt>
   0x000000000000126e <+37>:    mov    rax,QWORD PTR [rip+0x2dfb]        # 0x4070 <stdout@GLIBC_2.2.5>
   0x0000000000001275 <+44>:    mov    rdi,rax
   0x0000000000001278 <+47>:    call   0x1090 <fflush@plt>
   0x000000000000127d <+52>:    mov    eax,0x0
   0x0000000000001282 <+57>:    call   0x11b5 <read_int>
   0x0000000000001287 <+62>:    mov    DWORD PTR [rbp-0x4],eax
   0x000000000000128a <+65>:    cmp    DWORD PTR [rbp-0x4],0x12b9b0a1
   0x0000000000001291 <+72>:    je     0x12a9 <main+96>
   0x0000000000001293 <+74>:    lea    rdi,[rip+0xe1a]        # 0x20b4
   0x000000000000129a <+81>:    call   0x1030 <puts@plt>
   0x000000000000129f <+86>:    mov    eax,0x1
   0x00000000000012a4 <+91>:    jmp    0x138d <main+324>
   0x00000000000012a9 <+96>:    lea    rdi,[rip+0xe20]        # 0x20d0
   0x00000000000012b0 <+103>:   mov    eax,0x0
   0x00000000000012b5 <+108>:   call   0x1040 <printf@plt>
   0x00000000000012ba <+113>:   mov    rax,QWORD PTR [rip+0x2daf]        # 0x4070 <stdout@GLIBC_2.2.5>
   0x00000000000012c1 <+120>:   mov    rdi,rax
   0x00000000000012c4 <+123>:   call   0x1090 <fflush@plt>
   0x00000000000012c9 <+128>:   mov    eax,0x0
   0x00000000000012ce <+133>:   call   0x11b5 <read_int>
   0x00000000000012d3 <+138>:   mov    DWORD PTR [rbp-0x8],eax
   0x00000000000012d6 <+141>:   mov    edx,DWORD PTR [rbp-0x4]
   0x00000000000012d9 <+144>:   mov    eax,DWORD PTR [rbp-0x8]
   0x00000000000012dc <+147>:   add    eax,edx
   0x00000000000012de <+149>:   cmp    eax,0x1e996cc9
   0x00000000000012e3 <+154>:   je     0x12fb <main+178>
   0x00000000000012e5 <+156>:   lea    rdi,[rip+0xdc8]        # 0x20b4
   0x00000000000012ec <+163>:   call   0x1030 <puts@plt>
   0x00000000000012f1 <+168>:   mov    eax,0x1
   0x00000000000012f6 <+173>:   jmp    0x138d <main+324>
   0x00000000000012fb <+178>:   lea    rdi,[rip+0xdfe]        # 0x2100
   0x0000000000001302 <+185>:   call   0x1030 <puts@plt>
   0x0000000000001307 <+190>:   call   0x1080 <getchar@plt>
   0x000000000000130c <+195>:   mov    rdx,QWORD PTR [rip+0x2d6d]        # 0x4080 <stdin@GLIBC_2.2.5>
   0x0000000000001313 <+202>:   lea    rax,[rbp-0x50]
   0x0000000000001317 <+206>:   mov    esi,0x40
   0x000000000000131c <+211>:   mov    rdi,rax
   0x000000000000131f <+214>:   call   0x1060 <fgets@plt>
   0x0000000000001324 <+219>:   lea    rax,[rbp-0x50]
   0x0000000000001328 <+223>:   lea    rsi,[rip+0xd35]        # 0x2064
   0x000000000000132f <+230>:   mov    rdi,rax
   0x0000000000001332 <+233>:   call   0x1050 <strcspn@plt>
   0x0000000000001337 <+238>:   mov    BYTE PTR [rbp+rax*1-0x50],0x0
   0x000000000000133c <+243>:   lea    rax,[rbp-0x50]
   0x0000000000001340 <+247>:   lea    rsi,[rip+0xe09]        # 0x2150
   0x0000000000001347 <+254>:   mov    rdi,rax
   0x000000000000134a <+257>:   call   0x1070 <strcmp@plt>
   0x000000000000134f <+262>:   test   eax,eax
   0x0000000000001351 <+264>:   je     0x1366 <main+285>
   0x0000000000001353 <+266>:   lea    rdi,[rip+0xe26]        # 0x2180
   0x000000000000135a <+273>:   call   0x1030 <puts@plt>
   0x000000000000135f <+278>:   mov    eax,0x1
   0x0000000000001364 <+283>:   jmp    0x138d <main+324>
   0x0000000000001366 <+285>:   lea    rdi,[rip+0xe3b]        # 0x21a8
   0x000000000000136d <+292>:   call   0x1030 <puts@plt>
   0x0000000000001372 <+297>:   lea    rdi,[rip+0xe77]        # 0x21f0
   0x0000000000001379 <+304>:   call   0x1030 <puts@plt>
   0x000000000000137e <+309>:   mov    eax,0x0
   0x0000000000001383 <+314>:   call   0x11da <print_flag>
   0x0000000000001388 <+319>:   mov    eax,0x0
   0x000000000000138d <+324>:   leave
   0x000000000000138e <+325>:   ret
```

The first occurrence of such comparison is at `0x000000000000128a` where the input is compared to `0x12b9b0a1`, which is `314159265` in decimal. The next occurrence compares it with `0x1e996cc9`, which is `513371337`. The line right before this comparison adds the value of `edx` register to that of `eax` register; therefore this number should be the sum of the first answer and the second answer. Therefore, the second answer is `199212072`.

```text
E8M:/mnt/d/GitHub/angstromCTF2022/rev$ ./number-game 
Welcome to clam's number game!
Step right up and guess your first number: 314159265
That's great, but can you follow it up? 199212072
That was the easy part. Now, what's the 42nd number of the Maltese alphabet?
s
Ha! I knew I would get you there!
```

The third question sounds nonsensical (Google search result suggests that it's a Monty Python reference), and it compares the user input with a string. You can find the string by using a decompiler or debugging tools like GDB-peda.

```text
   0x555555555347 <main+254>:   mov    rdi,rax
=> 0x55555555534a <main+257>:   call   0x555555555070 <strcmp@plt>
   0x55555555534f <main+262>:   test   eax,eax
   0x555555555351 <main+264>:   je     0x555555555366 <main+285>
   0x555555555353 <main+266>:   lea    rdi,[rip+0xe26]        # 0x555555556180
   0x55555555535a <main+273>:   call   0x555555555030 <puts@plt>
Guessed arguments:
arg[0]: 0x7fffffffdc00 ("niubioblkgbk")
arg[1]: 0x555555556150 ("the airspeed velocity of an unladen swallow")
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdc00 ("niubioblkgbk")
```

The final answer is `the airspeed velocity of an unladen swallow`.

```text
/mnt/d/GitHub/angstromCTF2022/rev$ nc challs.actf.co 31334
Welcome to clam's number game!
Step right up and guess your first number: 314159265
That's great, but can you follow it up? 199212072
That was the easy part. Now, what's the 42nd number of the Maltese alphabet?
the airspeed velocity of an unladen swallow
How... how did you get that? That reference doesn't even make sense...
Whatever, you can have your flag I guess.
actf{it_turns_out_you_dont_need_source_huh}
```

**Flag: `actf{it_turns_out_you_dont_need_source_huh}`**

## uninspired (100 pts)

> clam has no more inspiration :( [maybe help him get some?](rev/uninspired)

The program asks for an input and determine its reaction.

```text
/mnt/d/GitHub/angstromCTF2022/rev$ ./uninspired 
there's no more inspiration :(
666666666666666
that's not very inspiring :(
```

Below is the decompiled code of the program.

```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int insp_len; // eax
  char *insp_ptr; // rdx
  unsigned __int8 trueinsp; // al
  __int64 i; // rax
  char insp[10]; // [rsp+0h] [rbp-48h] BYREF
  char term; // [rsp+Ah] [rbp-3Eh] BYREF
  __int128 buf[2]; // [rsp+10h] [rbp-38h] BYREF
  __int64 v11; // [rsp+30h] [rbp-18h]

  puts("there's no more inspiration :(");
  fgets(insp, 16, stdin);
  insp_len = strcspn(insp, "\n");
  insp[insp_len] = 0;
  if ( insp_len == 10 )
  {
    v11 = 0LL;
    insp_ptr = insp;
    memset(buf, 0, sizeof(buf));
    do
    {
      trueinsp = *insp_ptr - 48;
      if ( trueinsp > 9u )
      {
        puts("I don't like your inspiration :(");
        return 1;
      }
      ++insp_ptr;
      ++*((_DWORD *)buf + (char)trueinsp);
    }
    while ( insp_ptr != &term );
    i = 0LL;
    while ( *((_DWORD *)buf + i) == insp[i] - 48 )
    {
      if ( ++i == 10 )
      {
        puts("yay I'm inspired now, have a flag :)");
        print_flag((__int64)insp);
        return 0;
      }
    }
    puts("that's not good inspiration :(");
    return 1;
  }
  else
  {
    puts("that's not very inspiring :(");
    return 1;
  }
}
```

In order to get the flag, the input should satisfy all of the 3 requirements below:

1. The input length should be exactly 10.
2. Each letter of the input should be a number (`[0-9]`).
3. Each number should be equal to the frequency of the index of the number's position, which starts from 0.

Below is one of the possible solutions that satisfies all three conditions:

|**Number** |0|1|2|3|4|5|6|7|8|9|
|----|----|----|----|----|----|----|----|----|----|---|
|**Frequency**|6|2|1|0|0|0|1|0|0|0|

```text
M:/mnt/d/GitHub/angstromCTF2022/rev$ ./uninspired 
there's no more inspiration :(
6210001000
yay I'm inspired now, have a flag :)
actf{ten_digit_numbers_are_very_inspiring}
```

**Flag: `actf{ten_digit_numbers_are_very_inspiring}`**

## Beam (100 pts)

> Elixir needs more appreciation. Here's a [beam file](rev/Elixir.Angstrom.CLI.beam).
>
> Connect to it at `nc challs.actf.co 31400`.

The program asks a password and determines whether or not it will print the flag.

```text
/mnt/d/GitHub/angstromCTF2022/rev$ nc challs.actf.co 31400
Password: fdghfh
Sorry, no flag for you
```

The beam file can be analyzed by Erlang's `beam_disasm` command or other tools like VS Code's [BEAMdasm](https://marketplace.visualstudio.com/items?itemName=Valentin.beamdasm), which shows less confusing disassembly result.

```text
//Function  Elixir.Angstrom.CLI:check/0
label08:  func_info            Elixir.Angstrom.CLI check 0 //line lib/angstrom.ex, 20
label09:  allocate             0 0
          call                 0 label14 //line lib/angstrom.ex, 22
          call_ext             1 Elixir.String:to_charlist/1 //line lib/angstrom.ex, 23
          test_heap            . 1
          make_fun3            0 X[1] []
          call_ext             2 Elixir.Enum:map/2 //line lib/angstrom.ex, 24
          is_eq_exact          label10 X[0] gjsfxpslt
          call_last            0 label12 0
label10:  move                 Sorry, no flag for you X[0]
          call_ext_last        1 Elixir.IO:puts/1 0 //line lib/angstrom.ex, 28

//Function  Elixir.Angstrom.CLI:get_flag/0
label11:  func_info            Elixir.Angstrom.CLI get_flag 0 //line lib/angstrom.ex, 32
label12:  allocate             0 0
          move                 flag.txt X[0]
          call_ext             1 Elixir.File:read!/1 //line lib/angstrom.ex, 33
          call_ext_last        1 Elixir.IO:puts/1 0 //line lib/angstrom.ex, 34

//Function  Elixir.Angstrom.CLI:get_input/0
label13:  func_info            Elixir.Angstrom.CLI get_input 0 //line lib/angstrom.ex, 37
label14:  allocate             0 0
          move                 Password:  X[0]
          call_ext             1 Elixir.IO:gets/1 //line lib/angstrom.ex, 38
          call_ext_last        1 Elixir.String:trim/1 0 //line lib/angstrom.ex, 39

//Function  Elixir.Angstrom.CLI:main/0
label15:  func_info            Elixir.Angstrom.CLI main 0 //line lib/angstrom.ex, 16
label16:  move                 nil X[0]
          call_only            1 label18

//Function  Elixir.Angstrom.CLI:main/1
label17:  func_info            Elixir.Angstrom.CLI main 1 //line lib/angstrom.ex, 16
label18:  call_only            0 label09

//Function  Elixir.Angstrom.CLI:module_info/0
label19:  func_info            Elixir.Angstrom.CLI module_info 0
label20:  move                 Elixir.Angstrom.CLI X[0]
          call_ext_only        1 erlang:get_module_info/1

//Function  Elixir.Angstrom.CLI:module_info/1
label21:  func_info            Elixir.Angstrom.CLI module_info 1
label22:  move                 X[0] X[1]
          move                 Elixir.Angstrom.CLI X[0]
          call_ext_only        2 erlang:get_module_info/2

//Function  Elixir.Angstrom.CLI:-check/0-fun-0-/1
label23:  func_info            Elixir.Angstrom.CLI -check/0-fun-0- 1 //line lib/angstrom.ex, 24
label24:  gc_bif2              label00 1 erlang:+/2 X[0] 1 X[0]
          return              
          int_code_end        
```

The functions `check` and `-check/0-fun-0-` are interesting here. `check` hands over the user input to `-check/0-fun-0-`, which adds 1 to each letter of the input and returns the result to `check`, which compares it to `gjsfxpslt`. Therefore, the each letter of the user input should be one letter ahead of each letter of the comparison string.

|Check|Input|
|-----|-----|
|g|f|
|j|i|
|s|r|
|f|e|
|x|w|
|p|o|
|s|r|
|l|k|
|t|s|

The password that you should enter is `fireworks`.

```text
8M:/mnt/d/GitHub/angstromCTF2022/rev$ nc challs.actf.co 31400
Password: fireworks
actf{elixir_is_awesome}
```

**Flag: `actf{elixir_is_awesome}`**
