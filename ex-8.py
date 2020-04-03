liczby = []

max = 10

while max > 0:
    liczba = float(input("Podaj liczbe: "))
    liczby.append(liczba)
    max -= 1

print("Lista:", liczby)