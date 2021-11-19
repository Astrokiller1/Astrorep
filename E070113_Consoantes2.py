import sys
import math

numCaracteres=10
numvog=0
letra= str('/0')
numCons=0
frase=""
numletras=0

print()
print("Insira uma frase : ")
frase = input()

for contador in range(0, len(frase),1):
    letra=frase[contador]
    if (letra.isalpha()):
        print("Inseriu um caractere alfabético!!")
        numletras +=1
        letra = letra.lower()
        if (letra=='a' or letra == 'e' or  letra=='i' or letra=='o' or letra=='u') :
            numvog +=1
        else: numCons +=1

print("O numero de Consoantes que compoem a frase é : ",numCons)
print("O numero de Vogais que compoem a frase é : ",numvog)
print("O numero de Letras que compoem a frase é : ",numletras)