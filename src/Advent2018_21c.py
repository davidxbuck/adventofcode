def main():
    A=B=C=D=E=0
    XX = 0
    E = 0
    while True:
        D = E | 65536
        E = 707129
        while True:
            XX += 1
            C = D & 255
            E = E + C
            E = E & 16777215
            E *= 4
            E = E & 16777215
            print(XX, A, B, C, D, E)
            if XX > 256: return
            if 256 > D:
                print(D)
                if XX > 256: return
                if E == A:
                    return
            C = 0
            while True:
                B = C + 1
                B *= 256
                if B > D:
                    D = C
                break  # continue $2
                C += 1


main()
