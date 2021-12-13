# Wykorzystując funkcje, proszę napisać program, który będzie kalkulatorem dla funkcji trygonometrycznych: sin(), cos(), tg(), ctg(). 
# Wartości tych funkcji powinne być zapisane i odczytywane z pliku na potrzeby wykonywanych obliczeń. 
# Należy uwzględnić następujące wartości: 
# 0 (0°), π/6 (30°), π/4 (45°), π/3 (60°), π/2 (90°), π (180°), 2π (360°). 
# Proszę przygotować przypadki użycia dla tych funkcji.

def sin(kat):
    filepath = "F:\DOMINIK\Studia\WDI\WDI\Labolatorium_10\sin.txt" #ścieżka do pliku
    f = open(filepath, "r", encoding="utf-8") # otwieranie pliku tylko z odczytywaniem
    for line in f:
        if kat in line:
            print(line, end = "")
            break
    f.close() #zamknięcie pliku

def cos(kat):
    filepath = "F:\DOMINIK\Studia\WDI\WDI\Labolatorium_10\cos.txt"
    f = open(filepath, "r", encoding="utf-8")
    for line in f:
        if kat in line:
            print(line, end = "")
            break
    f.close()   

def tg(kat):
    filepath = "F:\DOMINIK\Studia\WDI\WDI\Labolatorium_10\\tg.txt"
    f = open(filepath, "r", encoding="utf-8")
    for line in f:
        if kat in line:
            print(line, end = "")
            break
    f.close()

def ctg(kat):
    filepath = "F:\DOMINIK\Studia\WDI\WDI\Labolatorium_10\ctg.txt"
    f = open(filepath, "r", encoding="utf-8")
    for line in f:
        if kat in line:
            print(line, end = "")
            break
    f.close()
    
while True:
    while True:
        kat = int(input("Proszę podać kąt (0°, 30°, 45°, 60°, 90°, 180°, 360°): "))
        if kat != 0 and kat != 30 and kat != 45 and kat != 60 and kat != 90 and kat != 180 and kat != 360:
            print("Program nie obsługuje podanej wartości")
        else:
            kat = str(kat)
            break

    while True:    
        funkcja = str(input("Proszę wybrać funkcję trygonometryczną (sin, cos, tg, ctg): " ))
        if funkcja != "sin" and funkcja != "cos" and funkcja != "tg" and funkcja != "ctg":
            print("Nie ma takiej funkcji")
        else:
            break
        
    match funkcja:
        case "sin":
            sin(kat)
        case "cos":
            cos(kat)
        case "tg":
            tg(kat)
        case "ctg":
            ctg(kat)   
    
    wyjscie = str(input("Jeśli chcesz zakończyć wpisz exit\nJeśli chcesz kontynuować wciśnij dowolny inny klawisz: "))

    match wyjscie:
        case "exit":
            break
        case _:
            continue