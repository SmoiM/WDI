#Należy stworzyć kalkulator umożliwiający dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, pierwiastkowanie, losowanie liczby z zakresu (w zależności od wybranego przez użytkownika trybu).
#Użytkownik powinien wpisywać liczby po kolei zatwierdzając je przy pomocy klawisza ENTER a następnie podać jeden z 6 symboli: +, -, *, /, **, ^, x.
#Po zakończeniu obliczeń powinien zostać wypisany komunikat: “Czy chcesz wprowadzić nowe dane?”. W zależności od odpowiedzi “T”/“N” należy umożliwić wprowadzenie nowych danych.
#W przypadku losowania liczby należy skorzystać z biblioteki random.
import random


odpowiedz = "T"

while odpowiedz == "T":

    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    liczba3 = 0
    dzialanie = str(input("wybierz tryb programu (+ (dodawanie), - (odejmowanie), * (mnożenie), / (dzielenie), ** (potęgowanie), ^ (pierwiastkowanie), x (losowa liczba z   przedziału)): "))

    match dzialanie:
        case "+":
            wynik = liczba1 + liczba2
            print(wynik)

        case "-":
            wynik = liczba1 - liczba2
            print(wynik)
        case "*":
            wynik = liczba1 * liczba2
            print(wynik)

        case "/":
            if liczba2 == 0:
                print("Nie dzielimy przez zero")
            else:
                wynik = liczba1 / liczba2
                print(wynik)

        case "**":
            wynik = liczba1 ** liczba2
            print(wynik)

        case "^":
            wynik1 = liczba1 ** (1 / 2)
            wynik2 = liczba2 ** (1 / 2)
            print(wynik1," ", wynik2)

        case "x":
            liczba3 = 0

            if liczba1 > liczba2:
                liczba3 = liczba2
                liczba2 = liczba1
                liczba1 = liczba3
                los = random.randint(liczba1, liczba2)
                print(los)
            else:
                los = random.randint(liczba1, liczba2)
                print(los)

    print("Czy chcesz wprowadzić nowe dane? Tak - wpisz T. Jeśli nie - wpisz N")
    odpowiedz = str(input())

    
    