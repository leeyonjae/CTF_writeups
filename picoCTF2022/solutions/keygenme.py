from hashlib import md5
import subprocess

v1 = 0
v18 = v1
v17 = 0x28
key = "picoCTF{br1ng_y0ur_0wn_k3y_"

v11 = 125
v2 = len(key)
v12 = md5(key.encode())
key += "." * (32 - len(key))

av11 = "deadbeef" # not actual memory address
v3 = len(av11)
v13 = md5(av11.encode())

key += v12.hexdigest()

v16 = v13.hexdigest()

v15 = "?"

v16 += key[:27]
v16 += key[45]
v16 += key[50]
v16 += v15
v16 += key[33]
v16 += key[46]
v16 += key[56]
v16 += key[58]
v16 += v15
v16 += chr(v11)
print(v16[32:])

aim = b"Enter your license key: That key is valid.\n"

for x in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    a = "picoCTF{br1ng_y0ur_0wn_k3y_19" + x + "36cd" + x + "}"    
    sp = subprocess.Popen(["../sources/keygenme/keygenme"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s = sp.communicate(a.encode())
    
    if aim in s[0]:
        print("Key:", a)
        
    
    sp.terminate()