n = input("Podaj wielocyfrowa liczbe calkowita: ")
wynik = 0
i = len(n)
while i > 0:
    wynik += int(n[i-1])
    i -= 1

print("Suma cyfr podanej liczby:", wynik)