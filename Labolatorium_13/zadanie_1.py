# Wykorzystując algorytm Euklidesa napisz funkcję wyznaczającą Największy Wspólny Dzielnik (NWD) wprowadzonych przez użytkownika liczb. 
# Zwizualizuj w konsoli rekurencyjny sposób działania programu.

# Przykłady NWD(645,363) = 3 NWD(420,1386) = 42 NWD(2891,1589) = 7 NWD(252,231) = 21 NWD(924,1105) = 1

def euklides (a, b, tab):
    a = abs(a)
    b = abs(b)
    if (b > a):
        cos = b
        b = a
        a = cos
    
    pom = a // b # dzielenie całkowite
    c = a - (pom * b) 
    nwd.append(b)
    print(a, " = ", a//b, " * ", b, " + ", c)

    a = b 
    b = c
   
    if c == 0:
        print("Największy wspólny dzielnik to ", tab[-1])
    else:
        euklides(a,b,tab)

while True: 
    a = int(input("Proszę podać pierwszą liczbę: "))
    if a != 0:
        break
    else:
        print("Podana wartość jest równa 0. Proszę podać inną wartość")
while True: 
    b = int(input("Proszę podać pierwszą liczbę: "))
    if b != 0:
        break
    else:
        print("Podana wartość jest równa 0. Proszę podać inną wartość")
nwd = []

euklides(a, b, nwd)