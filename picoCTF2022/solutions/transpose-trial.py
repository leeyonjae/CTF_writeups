# transpose-trial solution

corrupted = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"

blocks = []

for i in range(0,53,3):
    blocks.append(corrupted[i:i+3])

recovered = ""

for block in blocks:
    recovered += block[2]
    recovered += block[0]
    recovered += block[1]

print(recovered)