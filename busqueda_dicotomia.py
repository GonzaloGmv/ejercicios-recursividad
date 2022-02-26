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
            try:
                for i in range(len(tabla)):
                    tabla[i] = str(tabla[i])
                print("Los ordenaremos como tipo string")
            except:
                pass
    break
tabla.sort()