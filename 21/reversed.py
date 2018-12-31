r3 = 0
res = set()

while True:
    r4 = r3 | 0x10000
    r3 = 10649702
    while True:
        r5 = r4 & 0xFF
        r3 = r3 + r5
        r3 &= 0xFFFFFF
        r3 *= 65899
        r3 &= 0xFFFFFF
        if (256 > r4):

            if r3 not in res:
                res.add(r3)
                print(r3)
            break
        r4 = r4 // 256



