R0 = 0
R2 = 10551386
R5 = 1
while R5 <= R2:
    if not R2 % R5:
        R0 += R5
    R5 += 1

print(R0)
