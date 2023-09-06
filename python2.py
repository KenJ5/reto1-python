palabra = input("Escriba una frase o palabra: "+"\n")

for caracter in palabra:
        palabra = palabra.replace(" ","")
        palabra = palabra.casefold()
if (palabra==palabra[::-1]):
    print("Es palindromo")
else: 
    print("No es palindromo")
       


