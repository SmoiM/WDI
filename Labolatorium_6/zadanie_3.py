#ciąg Fibonacciego
fib1 = 0
fib2 = 1
fib3 = fib1 + fib2
iloczyn = 0

liczba = int(input("Podaj liczbę: "))

while iloczyn <= liczba:
    iloczyn = fib1 * fib2
    fib1=fib2
    fib2=fib3
    fib3 = fib1 + fib2
    if iloczyn == liczba:
        print("Ta liczna jest iloczynem dwóch dwóch wyrazów ciągu Fibonacciego")