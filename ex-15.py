try:
    x = float(input("Podaj liczbe: "))
    print("Podano poprawnie liczbe.")
except ValueError:
    print("Podano inne znaki niz cyfry!")