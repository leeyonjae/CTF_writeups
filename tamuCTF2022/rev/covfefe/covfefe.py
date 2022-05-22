
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
