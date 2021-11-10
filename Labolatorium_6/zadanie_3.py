#ciąg Fibonacciego
fib1 = 0
fib2 = 1
fib3 = fib1 + fib2
iloczyn = 0

while True:
    try:
        liczba = int(input("Podaj liczbę: ")) 
        break
    except:
        print("Podane wyrażenie nie jest liczbą naturalną. Spróbuj ponownie")

while iloczyn <= liczba:
    iloczyn = fib1 * fib2
    fib1=fib2
    fib2=fib3
    fib3 = fib1 + fib2
    if iloczyn == liczba:
        print("Ta liczba jest iloczynem dwóch dwóch wyrazów ciągu Fibonacciego")
    #else:
    #    print("Ta liczba nie jest iloczynem dwóch dwóch wyrazów ciągu Fibonacciego")