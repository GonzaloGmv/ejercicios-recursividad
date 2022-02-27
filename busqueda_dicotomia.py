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