import random
bandera = []
for i in range(0,7):
    bandera.append('R')
for i in range(0,6):
    bandera.append('A')
for i in range(0,4):
    bandera.append('V')
random.shuffle(bandera)
print(bandera)

def ordenar(n, m, color):
    j = 0
    for i in range(n, m):
        j = i + 1
        if bandera[i] != color:
            otro_color = bandera[i]
            bandera[i] = color
            for i in range(j, 17):
                if bandera[i] == color:
                    bandera[i] = otro_color
                    break

ordenar(0,7,'R')
ordenar(7,11,'V')
print(bandera)