# ejercicios-recursividad

La dirección de github para este repositorio es: [ github](https://github.com/GonzaloGmv/ejercicios-recursividad)

### Ejercicio 1. Búsqueda por dicotomía en una tabla ordenada
El código de este ejercicio es el siguiente:
```
#Creacion de la tabla
while True:
    tabla = input("Escriba los elementos de su tabla separados por espacios: ")
    tabla = tabla.split()
    try:
        for i in range(len(tabla)):
            tabla[i] = int(tabla[i])
        print("Los ordenaremos como tipo int")
    except:
        try:
            for i in range(len(tabla)):
                tabla[i] = float(tabla[i])
            print("Los ordenaremos como tipo float")
        except:
            print("Los ordenaremos como tipo string")
    break
tabla.sort()

#Función para buscar en la tabla
def buscar(c, m, m0):
    if m >= 0 and m <= len(tabla):
        if type(c) == type(tabla[m]):
            if c == tabla[m]:
                print(c, "se encuentra en la posicion", m)
            elif c > tabla[m] and m >= m0:
                m0 = m
                buscar(c, m+1, m0)
            elif c < tabla[m] and m <= m0:
                m0 = m
                buscar(c, m-1, m0)
            else:
                print(c, "no esta en la tabla")
        else:
                print(c, "no esta en la tabla")
    else:
        print(c, "no esta en la tabla")

#Ejecucion del ejercicio
n = input("Escriba el valor de c: ")
try:
    n = int(n)
except:
    try:
        n = float(n)
    except:
        pass
buscar(n, int(len(tabla)/2), int(len(tabla)/2))
```

### Ejercicio 2. Palíndromos
Para realizar este ejercicio, he tenido que buscar las líneas 7 y 8 en internet, ya que yo no sabía sustituir los caracteres acentuados por su equivalente sin acento.

El código de este ejercicio es el siguiente:
```
import unicodedata

#Filtrar la frase
frase = input("Escriba la frase que quiere comprobar si es palindromo: ")
filtrada = frase.split()
filtrada = ''.join(filtrada)
trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
filtrada = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', filtrada).translate(trans_tab))
filtrada = filtrada.lower()

#Función parea reconocer palindromos
def palindromo(N, M):
    if N < M:
        if filtrada[N] == filtrada[M]:
            palindromo(N+1, M-1)
        else:
            print(frase, "no es palindromo")
    elif N > M:
        palindromo(N, M+1)
    else:
        if filtrada[N] == filtrada[M]:
            print(frase, "es palindromo")
        else:
            print(frase, "no es palindromo")

#Ejecucion del ejercicio
m = len(filtrada)
n = 0
palindromo(n, m-1)
```

### Ejercicio 3. La bandera de Dijkstra
El código de este ejercicio es el siguiente:
```
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
print("Esta es la bandera desordenada: ")
print(bandera, '\n')

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
print("Esta es la bandera ordenada: ")
print(bandera)
```
