import sys
import math

resposta = '\0'
numNotas = 0
nota=0
soma = 0
maximo = 0

print()
print("Insira um conjunto de notas   : ")
contador = 0
while contador < 255:
    print("Insira a nota", (contador+1), " : ")
    nota =input()
    numNotas+=1
    if (contador ==0 or float(nota)>maximo):
        maximo = float(nota)
    print("Quer inserir outra nota (S/N) ? ")
    resposta=input()
    if (resposta =='n'  or resposta =='N'):
        break
    contador+=1
print("Maximo : ", maximo,".")
print()