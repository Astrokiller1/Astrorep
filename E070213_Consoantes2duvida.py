import sys
import math

numCaracteres=10
numvog=0
letra= str('/0')
numCons=0
frase=""
numletras=0
contador=len(frase)
print("Insira a frase para estudo : ")
frase=str(input())

while contador<len(frase):
    letra=frase[contador]
    if (letra.isalpha()):
        letra=letra.lower
        numletras +=1
        if letra[0]=='a' or letra[0]=='e'or letra[0]=='o' or letra[0]=='i' or letra[0]=='u':
            numvog+=1
        else:numCons+=1

print("O numero de Consoantes que compoem a frase é : ",numCons)
print("O numero de Vogais que compoem a frase é : ",numvog)
print("O numero de Letras que compoem a frase é : ",numletras)