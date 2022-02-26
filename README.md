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
def buscar(c, m):
    if type(c) == type(tabla[m]) and m >= 0 and m <= len(tabla):
        if c == tabla[m]:
            print(c, "se encuentra en la posicion", m)
        elif c > tabla[m]:
            buscar(c, m+1)
        elif c < tabla[m]:
            buscar(c, m-1)
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
buscar(n, int(len(tabla)/2))
```
