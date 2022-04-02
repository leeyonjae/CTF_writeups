# substitution 0 solution

enc = open("../sources/substitution0.txt", "r")

sub_upper = "EKSZJTCMXOQUDYLFABGPHNRVIW"
sub_lower = "ekszjtcmxoqudylfabgphnrviw"

alp_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_lower = "abcdefghijklmnopqrstuvwxyz"

for line in enc.readlines():
    prnt = ""
    for ch in line:
        if ch in sub_upper:
            prnt += alp_upper[sub_upper.find(ch)]
        elif ch in sub_lower:
            prnt += alp_lower[sub_lower.find(ch)]
        else:
            prnt += ch
    print(prnt)
