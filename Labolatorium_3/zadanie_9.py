#Stworzyć aplikację symulującą bankomat i wpłatomat.
#Użytkownik może wykonać trzy operacje: wpłata, wypłata, sprawdzić saldo.
#Należy przechowywać saldo.
#Przed każdą operacją należy zapytać użytkownika o PIN.
#Użytkownik nie może wybrać większej kwoty niż ta na koncie.
#Użytkowanie rozpoczyna się od podania typu operacji.
#Po każdej operacji powinien zostać wypisany komunikat: “Co chcesz zrobić w kolejnym kroku?”. (Użytkownik może też zakończyć korzystanie z programu).

saldo = 500.00
pin = '1234'
wyjscie = 0

print("BANKOMAT I WPŁATOMAT\n")

while wyjscie != 1:
    print("\nJeśli chcesz wpłacić pieniądze, wybierz: 1\nJeśli chcesz wypłacić pieniądze, wybierz: 2\nJeśli chcesz sprawdzić saldo, wybierz: 3\nJeśli chcesz wyjść, wybierz: 4\n")
   
    wybor = str(input("Proszę wybrać operację: "))
    
    match wybor:
        case "1":
            print("\nProszę podać kod pin: ")
            pinpod = str(input())

            if pinpod == pin:
                wplata = float(input("\nPodaj kwotę, jaką chcesz wpłacić: "))
                saldo += wplata
            else:
                print("\nWprowadzony pin jest niepoprawny")

        case "2":
            print("\nProszę podać kod pin: ")
            pinpod = str(input())

            if pinpod == pin:
                wyplata = float(input("\nPodaj kwotę, jaką chcesz wypłacić: "))

                if wyplata > saldo:
                    print("\nOperacja nie powiodła się. Zbyt mało środków na koncie")
                else:    
                    print("\nWypłacono z konta środki w wysokości %0.2f" %wyplata )
                    saldo -= wyplata
            else:
                print("\nWprowadzony pin jest niepoprawny") 

        case "3":
            print("\nProszę podać kod pin: ")
            pinpod = str(input())

            if pinpod == pin:
                print("\nStan Twojego konta wynosi %0.2f" %saldo,)
            else:
                print("\nWprowadzony pin jest niepoprawny")

        case "4":
            print ("\nDziękujemy za skorzystanie z naszego bankomatu")
            wyjscie += 1
        case _:
            print("\nNie ma takiej operacji. Spróbuj jeszcza raz")