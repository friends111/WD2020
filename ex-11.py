import sys

h = int(input("Podaj wysokosc diamentu (liczba nieparzysta od 3 do 9): "))
if not h % 2 or not 3 <= h <= 9:
    print("Wysokosc diamentu jest niepoprawna.")
    quit()

for i in range(1, h, 2):
    for x in range(h//2 - i//2):
        sys.stdout.write(' ')
    for x in range(i):
        sys.stdout.write('o')
    sys.stdout.write('\n')
for i in range(h, 0, -2):
    for x in range(h//2 - i//2):
        sys.stdout.write(' ')
    for x in range(i):
        sys.stdout.write('o')
    sys.stdout.write('\n')