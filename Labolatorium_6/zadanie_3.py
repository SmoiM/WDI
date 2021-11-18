#Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
#
#Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
#
#Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.

#Zdefiniowanie wyjątku
class NegativeNumberError(Exception): 
    pass 
class TooBigNumberError(Exception): 
    pass

#ciąg Fibonacciego
fib1 = 0
fib2 = 1
fib3 = fib1 + fib2

#zdefiniowanie pustej listy
tab = []

n = 1000000
#Dodawanie elementów do listy
while fib1 <= n:
    tab.append(fib1) 
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2


#zmienne pomocnicze do listy
i = 0
j = 1
dlugosc = len(tab)

#pobieranie liczby od użytkownika z zagwarantowaniem, że jest to liczba naturalna
while True:
    try:
        liczba = int(input("Podaj liczbę: "))
        if liczba < 0:
            raise NegativeNumberError
        if liczba > tab[dlugosc - 2] * tab[dlugosc - 1]:
            raise TooBigNumberError
        break
    
    except NegativeNumberError: 
        print("Liczba nie jest naturalna; jest mniejsza od zera") 
    except TooBigNumberError: 
        print("Wprowadzona liczba jest za duża. Wpisz mniejszą")

#sprawdzenie czy liczba jest iloczynem dwówch wyrazów ciągu Fibonacciego
while i <= dlugosc :
    iloczyn = tab[i] * tab[j]
    if iloczyn == liczba:
        print("Ta liczba jest iloczynem dwóch wyrazów ciągu Fibonacciego: ", tab[i], " ", tab[j])
        break
    else:
        if j < (dlugosc - 1):
            j += 1
        else:    
            i += 1
            if i < (dlugosc - 1):
                j = i + 1

    #wykona się, gdy tab[i] to ostatni element listy 
    if i == (dlugosc - 1):
        if iloczyn == liczba:
            print("Ta liczba jest iloczynem dwóch wyrazów ciągu Fibonacciego: ", tab[i], " ", tab[j])
        else:
            print("Ta liczba nie jest iloczynem żadnego z dwóch wyrazów ciągu Fibonacciego")
        break

#przykłady:
# 8, 10, 62 423 800 997 (26 i 29 wyraz ciągu), 62 423 800 998, 33 550, 121, 999 888