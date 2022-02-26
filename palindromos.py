import unicodedata
frase = input("Escriba la frase que quiere comprobar si es palindromo: ")
frase = frase.split()
frase = ''.join(frase)
trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
frase = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', frase).translate(trans_tab))
frase = frase.lower()
print(frase)