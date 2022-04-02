# flag-leak solving tool

recovered_flag = "ocip{FTCk43L_gn1g4lFff0_4tS_0_kc0155}c28"

real_flag = ""
block = ""

for l in recovered_flag:
    block = l + block
    if len(block) == 4:
        real_flag += block
        block = ""

print(real_flag)