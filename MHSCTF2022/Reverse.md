# Reverse Engineering

## Lemme In (30 pts)

> I want to join this secret club, but they have the weirdest passwords! I've managed to intercept the program they use to authenticate the passwords, but I don't know how to figure it out. Can you figure out the password for me?

The given program is a Python code:

```python
def roll(text):
  return text[::-1]  

def swoop(text):
  text = list(text)
  for i in range(len(text)):
    text[i] = chr(ord(text[i]) + (i % 5))
  return ''.join(text)

password = input("Enter the password: ")
if swoop(roll(password)) == "}12u7#dvl{$`fos_4jwchb}jelg":
  print("Welcome in!")
else:
  print("Sorry, wrong password.")
```

`roll(text)`: According to Python docs,

> Negative values also work to make a copy of the same list in reverse order:

```python
  >>> L[::-1]
  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

It returns reversed `text`.

`swoop(text)`: It first listifies `text`. Then, for each `i`th letter in `text`, it increases the ASCII value by `(i % 5)`.

A `roll`ed `text` can be recovered by `roll`ing it again, but we need a new function to cancel the `swoop`.

```python
def unswoop(text):
  text = list(text)
  for i in range(len(text)):
    text[i] = chr(ord(text[i]) - (i % 5))
  return ''.join(text)

print("Correct password is: " + roll(unswoop("}12u7#dvl{$`fos_4jwchb}jelg")))
```

When it is run:

```text
Enter the password: (random input)
Sorry, wrong password.
Correct password is: flag{ah_th3_old_$witc#3r00}
```

**Flag: `flag{ah_th3_old_$witc#3r00}`**

## Avengers Assemble (40 pts)

> The club I've been trying to get into has tightened up their security a lot! Can you get the password for me again? Note: the file uses the .asm extension which is not necessarily entirely accurate.

the file given is a disassembled Python program (excerpt below).

```python
  1           0 LOAD_CONST               0 (<code object main at 0x564456b6b9c0, file "example.py", line 1>)
              2 LOAD_CONST               1 ('main')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (main)

 15           8 LOAD_NAME                0 (main)
             10 CALL_FUNCTION            0
             12 POP_TOP
             14 LOAD_CONST               2 (None)
             16 RETURN_VALUE

```

To re-assemble it as best as I can:

```python
def main():
  inp = input("What's the password? ")
  pwd = ''

  for i in range(len(inp)):
    pwd += chr(ord(inp[i]) + (i % 7))
  
  comp = [102, 109, 99, 106, 127, 53, 116, 95, 122, 113, 120, 118, 100, 55, 51, 103, 57, 128]

  incor = False

  for i in range(len(pwd)):
    if pwd[i] != chr(comp[i]):
      incor = True
      break
  
  if incor == True:
    print('Incorrect password...')
  else:
    print('Welcome!')

main()
```

Apparently, the list `comp` contains the encrypted password. I wrote some additional lines of codes to crack the password:

```python
  ans = ''
  for i in range(len(comp)):
    ans += chr(ord(chr(comp[i])) - (i % 7))

  print(ans)
```

This code yields the password which is the flag.

**Flag: `flag{0n_your_13f7}`**
