#  5 seti 0 8 4           E = 0
#  6 bori 4 65536 3           D = E | 65536 (1000000000000000..)
#  7 seti 707129 0 4          E = 707129
#  8 bani 3 255 2             C = D & 255
#  9 addr 4 2 4               E = E + C
# 10 bani 4 16777215 4        E = E & 11111111111111
# 11 muli 4 65899 4           E *= 4
# 12 bani 4 16777215 4        E = E & 11111111111111
# 13 gtir 256 3 2             if 256 > D:
#                                 Value Out
#                                 go to 6
# 17 seti 0 7 2               C = 0
# 18 addi 2 1 1                   B = C + 1
# 19 muli 1 256 1                 B *= 256
# 20 gtrr 1 3 1                   if B > D:
# 26 setr 2 4 3                       D = C
# 27 seti 7 4 5                   go to 8
# 24 addi 2 1 2                   C += 1
# 25 seti 17 1 5                  go to 18
#
prev = []
A=B=C=D=E = 0
D = E | 65536
E = 707129
X = 0
while True:
    X += 1
    C = D & 255
    E = (((E + C) & 16777215) * 4) & 16777215
    print(A,B,C,D,E)
    if X > 5000: break
    if 256 > D:
        if E in prev:
            print("Found")
        print(E)
        prev.append(E)
        D = E | 65536
        E = 707129
        if len(prev) > 10: break
        continue
    C = 0
    while True:
        B = (C + 1) * 256
        if B > D:
            D = C
            break
        else:
            C += 1
            continue

