# Proszę napisać program wczytujący dwie macierze o ustalonych wymiarach m×n. 
# Dla wczytanych macierzy należy wykonać operacje: dodawania oraz odejmowania dwóch macierzy. Wymiar macierzy powinien być definiowany przez użytkownika.
import sys 

#Przykłady
#lista1 = [[1,2,3],[8,7,6],[5,4,3]]
#lista2 = [[7,6,5],[2,7,2],[9,2,3]]
#m = 3 # wiersze
#n = 3 # kolumny
#
#lista1 = [[1,2,3,4],[8,7,6,4],[1,5,4,3]]
#lista2 = [[7,6,5],[2,7,4,2],[9,2,5,3]]
#m = 3 # wiersze
#n = 4 # kolumny
#
#lista1 = [[1,2,3],[8,7,6],[5,4,3],[1,8,6]]
#lista2 = [[7,6,5],[2,7,2],[9,2,3]]
#m = 3 # wiersze
#n = 3 # kolumny
#
#lista1 = [[8,7,6],[5,4,3]]
#lista2 = [[7,6,5],[2,7,2],[9,2,3]]
#m = 3 # wiersze
#n = 3 # kolumny
#
#lista1 = [[8,7,64,3],[56,45,3,45],[5,74,840,1],[85,312,25,2],[4,55,21,384]]
#lista2 = [[7,213,6,60],[2,5,12,7],[9,789,123,2],[197,234,184,25],[135,123,3,45]]
#m = 5 # wiersze
#n = 4 # kolumny


lista1 = []
lista2 = []

m = int(input("Proszę podać ilość wierszy w macierzy: ")) # wiersze
n = int(input("Proszę podać ilość kolumn w macierzy: ")) # kolumny

# Tworzenie macierzy na wynik o rozmiarze m×n wypełnionej zerami
wynik = []
for i in range(m):
    wynik.append([0] * n)

# Funkcja tworząca macierz z podanych elementów (Każdy nowy wiersz w nowej linii)
def macierz(list, pomoc):
    pomoc = []
    for i in range(m):
        x = [int(x) for x in input("Wprowadź elementy danego wiersza macierzy: ").split()] # Rozdzielenie wpisanych liczb oddzielonych spacjami na pojedyncze elementy i utworzenie z nich listy
        pomoc.append(x)
        list.extend(pomoc) # Dodanie do listy kilku elementów jednocześnie
        pomoc = []

# Funkcja sprawdzająca, czy założenia dodawania i odejmowania macierzy są spełnione (Czy mają ten sam zdefiniowany wcześniej przez m oraz n rozmiar)
def check(rows, columns, m1, m2):
    length1, length2 = len(m1), len(m2) # Ilość wierszy w macierzach

    if (length1 != rows or length2 != rows):
        print ("Macierz posiada inną liczbę wierszy niż zdefiniowano")
        sys.exit(0) # Zakończenie działania programu

    for i in range (0, rows):
        length1, length2 = len(m1[i]), len(m2[i]) # Ilość elementów (kolumn) w wierszu

        if (length1 != columns or length2 != columns):
            print ("Przynajmniej jeden wiersz macierzy posiada inną liczbę elementów niż zdefiniowano")
            sys.exit(0) # Zakończenie działania programu

#Funkcja definiująca dodawanie macierzy
def dodawanie(m1, m2, m3):
    pom = []

    macierz(m1, pom)
    macierz(m2, pom)
    check(m,n,lista1, lista2)

    for q in range(0, m):
        for w in range (0, n):
            m3[q][w] = m1[q][w] + m2[q][w]

    print ("Dodawanie:\n", m1,"+\n", m2,"=\n", m3)

    m1.clear() # Usuwanie wszystkich elementów z tablicy
    m2.clear() # Usuwanie wszystkich elementów z tablicy

#Funkcja definiująca odejmowanie macierzy
def odejmowanie(m1, m2, m3): 
    pom = []

    macierz(m1, pom)
    macierz(m2, pom)
    check(m, n, lista1, lista2)

    for q in range(0, m):
        for w in range (0, n):
            m3[q][w] = m1[q][w] - m2[q][w]

    print ("Odejmowanie:\n",m1,"-\n", m2,"=\n", m3)

    m1.clear() # Usuwanie wszystkich elementów z tablicy
    m2.clear() # Usuwanie wszystkich elementów z tablicy
    
dodawanie(lista1, lista2, wynik)
odejmowanie(lista1, lista2, wynik)