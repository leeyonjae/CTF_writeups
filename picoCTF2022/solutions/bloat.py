# bloat.py code deobfusticated

import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

def check_input(arg_input):
  if arg_input == "happychance":
    return True
  else:
    print("That password is incorrect")
    sys.exit(0)
    return False

def decode_flag(enc):
  return decrypt(enc.decode(), "rapscallion")

def begin_app():
  return input("Please enter correct password for flag: ")

def load_flag():
  return open('flag.txt.enc', 'rb').read()

def greet():
  print("Welcome back... your flag, user:")
  
def decrypt(encrypted, key):
    arg433 = key
    i = 0
    while len(arg433) < len(encrypted):
        arg433 = arg433 + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(encrypted,arg433)])
raw_flag = load_flag()
arg_input = begin_app()
check_input(arg_input)
greet()
key = decode_flag(raw_flag)
print(key)
sys.exit(0)

