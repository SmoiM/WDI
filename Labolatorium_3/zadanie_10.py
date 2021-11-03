#Należy stworzyć kalkulator umożliwiający dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, pierwiastkowanie, losowanie liczby z zakresu (w zależności od wybranego przez użytkownika trybu).
#Użytkownik powinien wpisywać liczby po kolei zatwierdzając je przy pomocy klawisza ENTER a następnie podać jeden z 6 symboli: +, -, *, /, **, ^, x.
#Po zakończeniu obliczeń powinien zostać wypisany komunikat: “Czy chcesz wprowadzić nowe dane?”. W zależności od odpowiedzi “T”/“N” należy umożliwić wprowadzenie nowych danych.
#W przypadku losowania liczby należy skorzystać z biblioteki random.
import random


odpowiedz = "T"

while odpowiedz == "T":

    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
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
            los = random.randint(liczba1, liczba2)
            print(los)

    print("Czy chcesz wprowadzić nowe dane? Tak - wpisz T. Jeśli nie - wpisz N")
    odpowiedz = str(input())

    
    