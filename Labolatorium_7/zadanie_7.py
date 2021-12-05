#Proszę napisać program, który umożliwia obliczenie wartości N! dla N zakresu od 1 do M, gdzie M jest wartością wpisaną przez użytkownika. Należy obsłużyć wyjątek, gdy użytkownik podaje liczbę mniejszą od 1 oraz taki gdy M jest większe od 1000000. Program powinien też wypisywać na końcu różnice pomiędzy kolejnymi wartościami N!.

class NegativeNumberError(Exception): 
    pass 
class TooBigNumberError(Exception): 
    pass 

while True:
    try:
        liczba = int(input("Proszę podać liczbę naturalną większą od 0 i mniejszą od 1 000 000: "))
        if liczba < 0:
            raise NegativeNumberError
        if liczba > 1000000:
            raise TooBigNumberError
        break
    except NegativeNumberError:
        print("Podana liczba jest ujemna")
    except TooBigNumberError:
        print("Podana liczba jest większa od 1 000 000")


#zmienna do silni
i = 1
#zmienna do różnicy
j = 1
#zmienna do wyświetlania
w = 0

iloczyn = 1

#puste listy
silnia = []
roznica = []

#liczy silnię i zapisuje wynik i! dla 1 < i <= liczba 
while i <= liczba:
    iloczyn = iloczyn * i
    silnia.append(iloczyn)
    i += 1

print("%i! wynosi:" % liczba, iloczyn)
#Ewentualnie: print(liczba, "! wynosi: ", iloczyn) 
# Ale wtedy jest spacja po liczbie

#oblicza różnice dwóch kolejnych silni
while j <= (liczba - 1):
    wynik = silnia[j] - silnia[j-1]
    #Można też tak: print("Różnica wyrazu", j, "i", j-1, ":",silnia[j], "-", silnia[j-1], "wynosi:", wynik)
    # Wtedy bez append
    roznica.append(wynik)
    j += 1

#wyświetla różnice dwóch kolejnych silni
while w < (liczba - 1):
    print("%i! - %i! wynosi:" %((w + 2), (w + 1)), roznica[w], )
    w +=1

#Nie polecam testować dla 1 000 000 i tym podobnych
#dla 1 000 wciąż OK, dla 10 000 też działa 
#ale i tak są to zbyt duże liczby, żeby je czytać
#dla 100 000 już nie


