import sys

n = int(input("Podaj wysokosc wiezy: "))

for i in range(1, n+1):
    for x in range(i):
        sys.stdout.write('A')
    sys.stdout.write('\n')
    if i >= 10:
        print("Wieza nie moze byc wieksza niz 10")
        break