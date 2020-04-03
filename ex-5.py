a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))
c = float(input("Podaj trzecia liczbe: "))

if (0 < a <= 10) and (a > b or b < c):
    print("Warunki zostaly spelnione!")
else:
    print("Nie zostaly spelnione wszystkie warunki.")