import math

try:
    x = float(input("Podaj liczbe: "))
    print("Pierwiastek kwadratowy z tej liczby:", math.sqrt(x))
except ValueError:
    print("Nie mozna obliczyc rzeczywistego pierwiastka z liczby ujemnej.")