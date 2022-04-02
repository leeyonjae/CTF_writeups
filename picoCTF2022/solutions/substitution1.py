# substitution 1 solution

enc = open("../sources/substitution1.txt", "r")

# Final substitution table
alp_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_lower = "abcdefghijklmnopqrstuvwxyz"
sub_upper = "G.FITOVWCSDUYQLKHMEBR..ANP"
sub_lower = "g.fitovwcsduyqlkhmebr..anp"

for line in enc.readlines():
    print(line)
    prnt = ""
    for ch in line:
        if ch in alp_upper:
            prnt += sub_upper[alp_upper.find(ch)]
        elif ch in alp_lower:
            prnt += sub_lower[alp_lower.find(ch)]
        else:
            prnt += ch
    print(prnt)
