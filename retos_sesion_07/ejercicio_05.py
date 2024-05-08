# Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome la frase o palabra ejemplo "Anita lava la Tina" es verdad

frase = str(input("Ingrese una frase palíndroma: "))
frase = frase.replace(" ", "")
frase = frase.lower()

frase_invertida = frase[::-1]

if frase == frase_invertida:
    print("La frase es palíndroma")

else:
    print("La frase no es palíndroma")