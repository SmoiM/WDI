# Na szachownicy o wymiarach 100 na 100 umieszczamy N skoczków (N<100). Położenie skoczków jest opisywane przez tablicę:
#   dane = [(w1, k1), (w2, k2), (w3, k3), ..., (wN, kN)] 
# Proszę napisać funkcję, która zwróci położenie skoczków wzajemnie się szachujących. 
# Do funkcji należy przekazać położenie skoczków. 
# Należy zwizualizować rozkład skoczków na szachownicy. 
# Testy powinny uwzględniać między innymi:
#   Przypadek, w którym nie występuje szachowanie.
#   Przypadek, w którym szachują się dwa skoczki.
#   Przypadek, w którym szachują się więcej niż dwa skoczki.

# class Figury:
#     def __init__(self,ruchy ,polozenie):
#         self.ruchy = ruchy
#         self.polozenie = polozenie
        
#     def sk(self,ruchy, polozenie):
#         for j in range (len(polozenie)): # sprawdza każdą figurę
#             for i in range (len(ruchy)): # sprawdza każdy możliwy ruch
#                 skok = (polozenie[j][0] + ruchy[i][0],polozenie[j][1] + ruchy[i][1]) # położenie po wykonaniu ruchu
#                 if skok in polozenie: # sprawdza, czy po wykonaniu ruchu, skoczek natrafi na pole, na którym stoi inny skoczek
#                     print ("Skoczek na pozycji ", polozenie[j], "szachuje skoczka na pozycji ", skok)

# ruchy = [(1,-2),(2,-1),(2,1),(1,2),(-1,-2),(-2,-1),(-2,1),(-1,2)] # definicja ruchów skoczka
# polozenie = [(1,2),(3,3)] # lista wszystkich skoczków

# skoczek = Figury(ruchy, polozenie)
# skoczek.sk(ruchy, polozenie)

for i in range (10):
    for j in range (10):
        if j == 5:
            print (" x ", end = "")
        else:
            print (" o ", end = "")
            if j == 9:
                print("\n", end = "")