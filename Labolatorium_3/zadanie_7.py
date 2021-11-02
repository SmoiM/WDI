def liczbyfor():
    liczba1 = int(input("Prosze podac liczbe1: "))
    liczba2 = int(input("Prosze podac liczbe2: "))

    #zmienna pomocnicza
    liczba3 = 0

    if liczba1 > liczba2:
        liczba3 = liczba2
        #print(liczba1, liczba2, liczba3)
        liczba2 = liczba1
        #print(liczba1, liczba2, liczba3)
        liczba1 = liczba3
        #print(liczba1, liczba2, liczba3)
    
    if liczba2 - liczba1 + 1 > 20:
        srednia = (liczba1 + liczba2) / 2
        print("Średnia wynosi %f" %srednia)
        minimum = int(srednia) - 3
        maximum = int(srednia) + 3

        # Czy liczba jest całkowita
        if srednia - int(srednia) == 0:
            for liczba1 in range (minimum, maximum + 1):
                if liczba1 == srednia:
                    liczba1 += 1
                else:
                    print ("%d\n" %liczba1)
                    liczba1 += 1
        else:
            for liczba1 in range (minimum, maximum):
                print ("%d\n" %liczba1)
                liczba1 += 1
    else:    
        for liczba1 in range (liczba1, liczba2 + 1):
            print ("%d\n" %liczba1)
            liczba1 += 1
    return


def liczbywhile():
    liczba1 = int(input("Prosze podac liczbe1: "))
    liczba2 = int(input("Prosze podac liczbe2: "))

    #zmienna pomocnicza
    liczba3 = 0

    if liczba1 > liczba2:
        liczba3 = liczba2
        liczba2 = liczba1
        liczba1 = liczba3

    if liczba2 - liczba1 + 1 > 20:
        srednia = (liczba1 + liczba2) / 2
        print("Średnia wynosi %f" %srednia)
        
        
        if srednia - int(srednia) == 0:
            liczba1 = srednia - 3
            while liczba1 <= srednia + 3:
                if liczba1 == srednia:
                    liczba1 += 1
                else:
                    print ("%d\n" %liczba1)
                    liczba1 += 1
        else:
            liczba1 = int(srednia) - 2
            while liczba1 <= int(srednia) + 3:
                print ("%d\n" %liczba1)
                liczba1 += 1
    else:

        while liczba1  <= liczba2:
            print ("%d\n" %liczba1)
            liczba1 += 1
    return

liczbywhile()
#liczbyfor()


