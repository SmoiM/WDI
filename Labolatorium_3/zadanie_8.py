wysokosc = int(input("Proszę podać wysokość choinki: "))
rzad = 0
dodatek = 0
galaz = "*"
spacja = wysokosc -1

while rzad < wysokosc:
    if rzad == 0:
        print((spacja-1)*" ", "X"*(2*rzad+1))
    elif rzad != 0 and rzad != wysokosc - 1:
        print((spacja-1)*" ", galaz*(2*rzad+1)) 
    else:
        print(galaz*(2*rzad+1)) 

    rzad += 1
    spacja -= 1

print((rzad-2)*" ","U")

#galaz = "*"
#linia = 3 * galaz
#print(linia)