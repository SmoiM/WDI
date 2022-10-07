wysokosc = int(input("Proszę podać wysokość choinki: "))
rzad = 0
galaz = "*"
spacja = wysokosc - 1

if wysokosc < 0 or wysokosc == 0:
    print("wysokość musi być liczbą całkowitą większą od zera!!!")
    quit()

while rzad < wysokosc:
    if rzad == 0:
        print((spacja - 1)*" ", "X" * (2 * rzad + 1))
    elif rzad != 0 and rzad != wysokosc - 1:
        print((spacja - 1) * " ", galaz*(2 * rzad + 1)) 
    else:
        print(galaz * (2 * rzad + 1)) 

    rzad += 1
    spacja -= 1

print((rzad - 2) * " ", "U")