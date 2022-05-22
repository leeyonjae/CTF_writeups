flag = open("./scheme.txt", "r").read().split("\n")

url = "https://www.gamergeeks.net/apps/minecraft/banner-maker#mcb=a14"

for f in flag:
    patterns = f.split("}")
    out = ""
    for p in patterns:
        out += p
    
    print(url + out)
