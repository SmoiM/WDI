liczba = int(input("Podaj liczbę: "))
pom = 1

if liczba < 0:
    liczba = - liczba
    while pom <= liczba:
        dzielnik = liczba / pom
        if dzielnik - int(dzielnik) == 0:
            print("+/-", pom)
            pom += 1
        else:
            pom += 1
else:
    while pom <= liczba:
        dzielnik = liczba / pom
        if dzielnik - int(dzielnik) == 0:
            print(pom)
            pom += 1
        else:
            pom += 1
