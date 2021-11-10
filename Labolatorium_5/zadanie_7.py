liczba = int(input("Podaj liczbę: "))
#zmienna pomocnicza, ktora pełni funkcję dzielnika
pom = 1

#wartość bezwzględna z liczby
liczba = abs(liczba)

while pom <= liczba / 2:
    #operacja modulo - reszta z dzielenia
    dzielnik = liczba % pom

    if dzielnik == 0:
        print(pom)
        pom += 1
    else:
        pom += 1

print(liczba)


