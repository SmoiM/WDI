#Proszę napisać program, który wypełnia N-elementową listę trzycyfrowymi liczbami pseudolosowymi a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w liście, dla którego w liście występuje również rewers tego ciągu. 
# Na przykład dla listy: 
#[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] 
# odpowiedzią jest liczba 4. 
# Dla podciągu [9,3,1,7] rewersem jest [7,1,3,9].

#ZAŁOŻENIE DO ZADANIA
#
#Dla podciągu [914,312,143,723] rewersem nie jest [723,143,312,914]
#Dla podciągu [914,312,143,723] rewersem jest [327,341,213,419], czyli liczby, które powstaną po zamienieniu miejscami cyfr podciągu (pierwsza cyfra staje się ostatnią, druga - przedostatnią, itd. )

import random

class NegativeNumberError(Exception): 
    pass

# Jeśli zmienne byłyby poza funkcją, należałoby przekazać je funkcji poprzez podanie potrzebnych zmiennych w definicji i wypisanie ich przy wywołaniu funkcji
# np. def funkcja(a): -> na wejściu funkcja potrzebuje zmiennej a (która poza definicją może mieć totalnie inną nazwę), ale musi mieć ten sam typ, co a
#   ...
# c = 4
# funkcja(c) 

def podciag():
    lista = [] # przechowuje cały ciąg liczb
    ciag = [] # przechowuje potemcjalny najdłuższy podciąg w danej iteracji pętli
    rewers = [] # przechowuje potemcjalny najdłuższy rewers w danej iteracji pętli
    maxciag = [] # przechowuje aktualnie najdłuższy podciąg mający rewers
    maxrew = [] # przechowuje aktualnie najdłuższy rewers mający podciąg

    while True:
        try:
            ilosc =int(input("Proszę podać ilość elementów listy: "))
            if ilosc < 0:
                raise NegativeNumberError
            break
        except NegativeNumberError:
            print("Podana liczba jest ujemna")    

# tworzenie listy z liczb pseudolosowych
    for i in range(0, ilosc):
        liczba = random.randint(100,999)
        lista.append(liczba)

    l = len(lista)
    max = 0 # przechowuje wartość długości podciągu w danej iteracji pętli
    maxmax = 0 # przechowuje największą wartość jaką osiągnął max

    for i in range (0, l):
        wsk = str(lista[i]) # zamiana wsk na stringa
        wsk = int(wsk[::-1]) # zmiana kolejności cyfr w wsk i zamiana go z powrotem na int
        for o in range (l - 1, i, -1): #pętla dekrementująca o 1 -> sprawdzamy ciąg od końca
            if lista[o] == wsk:
                ciag.append(lista[i])
                rewers.insert(0, lista[o]) # dodawanie elementu na początek listy -> .insert(x,zmienna) x - indeks, na który wstawiamy
                max += 1
                i += 1
                wsk = str(lista[i]) # zamiana wsk na stringa
                wsk = int(wsk[::-1]) # zmiana kolejności cyfr w wsk i zamiana go z powrotem na int
            else:
                if len(ciag) > len(maxciag): # działa tylko wtedy, gdy nowy podciąg jest dłuższy od obecnie zapisanego
                    maxciag = ciag # na listach takie równości też działają
                    maxrew = rewers
                    maxmax = max
                ciag = [] # czyszczenie listy
                rewers = []
                max = 0
                
    print("Podciąg:", maxciag, "\nRewers:", maxrew, "\nDługość najdłuższego podciągu:" , maxmax)

podciag()
