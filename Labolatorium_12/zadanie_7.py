# Na szachownicy o wymiarach 100 na 100 umieszczamy N skoczków (N<100). Położenie skoczków jest opisywane przez tablicę:
#   dane = [(w1, k1), (w2, k2), (w3, k3), ..., (wN, kN)] 
# Proszę napisać funkcję, która zwróci położenie skoczków wzajemnie się szachujących. 
# Do funkcji należy przekazać położenie skoczków. 
# Należy zwizualizować rozkład skoczków na szachownicy. 
# Testy powinny uwzględniać między innymi:
#   Przypadek, w którym nie występuje szachowanie.
#   Przypadek, w którym szachują się dwa skoczki.
#   Przypadek, w którym szachują się więcej niż dwa skoczki.

import random

class Figury:      
    def sk(self, polozenie):
        p = False
        ruchy = [(1,-2),(2,-1),(2,1),(1,2),(-1,-2),(-2,-1),(-2,1),(-1,2)] # definicja ruchów skoczka
        for j in range (len(polozenie)): # sprawdza każdą figurę
            for i in range (len(ruchy)): # sprawdza każdy możliwy ruch
                skok = (polozenie[j][0] + ruchy[i][0],polozenie[j][1] + ruchy[i][1]) # położenie po wykonaniu ruchu
                if skok in polozenie: # sprawdza, czy po wykonaniu ruchu, skoczek natrafi na pole, na którym stoi inny skoczek
                    print ("Skoczek na pozycji ", polozenie[j], "szachuje skoczka na pozycji ", skok)
                    p = True
        if p == False:
            print("Nic się tu nie szachuje :(")


wybor = int(input("Proszę wybrać przypadek ustawienia skoczków na szachownicy:\n\t1 - dwa skoczki się szachują,\n\t2 - więcej niż dwa skoczki się szachują\n\t3 - nic się nie szachuje\n\t4 - losowe ustawienie n skoczków na planszy m na m\nWybór: "))

while True:
    match wybor:
        case 1:
            polozenie = [(1,1),(3,2),(10,20),(10,15),(5,10),(9,8),(10,2),(8,11),(7,2),(9,10),(6,7),(12,6),(6,18),(4,5),(18,3),(13,7),(4,15),(4,20),(19,13),(20,20),(1,20), (20,1)] # 2 skoczki się szachują
            plansza = 20 # wymiary szachownicy
            break
        case 2:
            polozenie = [(1,1),(1,2),(3,3),(10,15),(5,10),(9,9),(10,2),(8,11),(7,2),(9,10),(6,7),(12,5),(6,18),(4,5),(18,3),(13,7),(4,15),(4,20),(19,13)] # lista wszystkich skoczków (x,y) więcej niż 2 skoczki się szachują
            plansza = 20 # wymiary szachownicy
            break
        case 3:
            polozenie = [(1,1),(20,20),(1,20),(20,1), (15,4),(8,12),(10,6),(14,12),(10,10),(9,11),(6,7),(12,6),(6,18),(18,20),(20,10),(19,19),(18,18),(17,17),(2,19),(1,10)]
            plansza = 20 # wymiary szachownicy
            break
        case 4:
            skoczki = int(input("Podaj liczbę skoczków: "))
            polozenie = []
            plansza = int(input("Proszę podać wymiary planszy: "))
            for s in range(0,skoczki):
                x = random.randint(1,plansza)
                y = random.randint(1,plansza)
                a = (x,y)

                if a in polozenie:
                    while a in polozenie:
                        x = random.randint(1,plansza)
                        y = random.randint(1,plansza)
                        a = (x,y)
                    polozenie.append(a)    
                else:
                    polozenie.append(a)
            break

skoczek = Figury()
skoczek.sk(polozenie) # wywołanie metody z klasy 

f = open("Labolatorium_12\plansza.txt", "w")

for i in range (1, plansza + 1):
    for j in range (1, plansza + 1):
        krotka = (j, i)
        if krotka in polozenie and j == plansza:
            f.write(" S " + "\n" + '')
        elif krotka in polozenie:
            f.write(" S " +'') 
        else:
            f.write(" . "+'')
            if j == plansza:
                f.write("\n" + '')
            
f.close()


#_______________________________________________
# for i in range (0, plansza + 1):
#     for j in range (1, plansza + 1):
#         if i == 0:
#             f.write(" " + str(j) + " " + '')
#             #print(" " + str(j) + " ", end = '')
#             if j == plansza:
#                 f.write("\n"+'')
#                 #print("\n", end = '')
        
#         else:
#             krotka = (i, j)
#             if krotka in polozenie:
#                 f.write(" S " +'')
#                 #print(" S ", end = '')
#             else:
#                 f.write(" . "+'')
#                 #print(" . ", end = '')
#                 if j == plansza:
#                     f.write(" " + str(i) + "\n"+'')
#                     #print(" " + str(i) + "\n", end = '')