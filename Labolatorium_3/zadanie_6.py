#Podawanie liczb

liczba1 = int(input("Prosze podac liczbe1: "))
liczba2 = int(input("Prosze podac liczbe2: "))

#Wyświetlanie podanych liczb 
#print ("Wprowadzone przez Ciebie liczby to: %d i %d" %(liczba1, liczba2))

# Podane liczby
# Tylko po co
# Pewnie po nic


if (liczba1 and liczba2 < 0):
    print ("Obie liczby sa mniejsze od zera :( Koniec programu")
    exit()
elif (liczba1 < 0):
    liczba1 = - liczba1

elif (liczba2 < 0):
    liczba2 = - liczba2

# Lista działań
suma = liczba1 + liczba2
roznica = liczba1 - liczba2
iloczyn = liczba1 * liczba2
iloraz = liczba1 / liczba2
kwadrat1 = liczba1 ** 2
kwadrat2 = liczba2 ** 2
pierwiastek1 = liczba1 ** (1 / 2)
pierwiastek2 = liczba2 ** (1 / 2)

if (iloczyn == 10):
    print("Suma: %d\nRoznica: %d\n iloczyn :%d Yay!\n iloraz: %f\n kwadrat liczby pierwszej: %d\n kwadrat liczby drugiej: %d\n pierwiastak liczby pierwszej: %d\n pierwiastek liczby drugiej: %d\n" %(suma, roznica, iloczyn, iloraz, kwadrat1, kwadrat2, pierwiastek1, pierwiastek2) )
else:
    print("Suma: %d\nRoznica: %d\niloczyn :%d\niloraz: %f\nkwadrat liczby pierwszej: %d\nkwadrat liczby drugiej: %d\npierwiastak liczby pierwszej: %d\npierwiastek liczby drugiej: %d\n" %(suma, roznica, iloczyn, iloraz, kwadrat1, kwadrat2, pierwiastek1, pierwiastek2) ) 
