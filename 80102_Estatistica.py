import time
import numpy as np

media=0
resposta ='\0'

print()
print("Quantas notas quer inserir ? : ")
numNotas = int(input())
print()
notas = [0.0 for i in range(numNotas)]

while (resposta !='N' and resposta !='n'):
    notas = [0.0 for i in range(numNotas)]
    print()
    print("Insira um conjunto de ",numNotas, "notas.")
    for cValor in range(0,numNotas,1):
        print("Insira a nota " + format(cValor+1)+": ")
        notas[cValor]=float(input())
    print()
    print("processamento das entradas...")
    time.sleep(1)
    media=0
    for cValor in range(0,numNotas,1):
        media+= notas[cValor]/numNotas
    print("A média é : ", media)
    print("Quer inserir outras notas (S/N) : ")
    resposta=input()
print()
