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