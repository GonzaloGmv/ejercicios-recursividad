import random

#Creamos la bandera
bandera = []
for i in range(0,7):
    bandera.append('R')
for i in range(0,6):
    bandera.append('A')
for i in range(0,4):
    bandera.append('V')
random.shuffle(bandera)
print(bandera)

#Función para ordenar las fichas
def ordenar(n, m, color):
    if bandera[n] != color:
        otro_color = bandera[n]
        bandera[n] = color
        for i in range(n+1, 17):
            if bandera[i] == color:
                bandera[i] = otro_color
                break
        if n < m:
            ordenar(n+1, m, color)
    else:
        if n < m:
            ordenar(n+1, m, color)

#Ejecución del ejercicio
ordenar(0,6,'R')
ordenar(7,10,'V')
print(bandera)