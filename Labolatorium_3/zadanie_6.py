#Podawanie liczb

liczba1 = int(input("Prosze podac liczbe1: "))
liczba2 = int(input("Prosze podac liczbe2: "))

# Podane liczby
# Tylko po co
# Pewnie po nic

print ("Wprowadzone przez Ciebie liczby to: %d i %d" %(liczba1, liczba2))

if (liczba1 and liczba2 < 0):
    print ("Liczby sa mniejsze od zera")
if(liczba1 < 0):
    liczba1=-liczba1
