import sys
import math

numNotas=0
nota=0
media=0

print("Quantas notas pretende inserir ?")
numNotas = input()
print()
print("Insira um conjunto de", int(numNotas), " notas : ")
contador = 0

while contador < int(numNotas):
    print("Insira a nota ", (contador+1, ": "))
    nota = input()
    media += float(nota)/int(numNotas)
    contador +=1

print("Media : ", media,".")
print()
