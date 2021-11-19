import sys
import math
import array
import numpy as np
import time

numDespesas = 5
somaSemIVA= 0
somaComIVA=0
despesas = np.zeros(numDespesas)
despesas= [0.0 for i in range(numDespesas)]
taxasIVA=[0.0 for i in range(numDespesas)]

print()
print("Insira cinco despesas : ")
for cValor in range(0,numDespesas,1):
    print("Insira a despesa",(cValor+1), ": ")
    despesas[cValor] = input()
    print("Insira a taxa de IVA ", (cValor+1)), ": "
    taxasIVA[cValor] = input()

print()
print("Processamento das entradas ...")
time.sleep(1)
for cValor in range (0,numDespesas,1):
    somaSemIVA+= float(despesas[cValor])
    somaComIVA+= (1+float(taxasIVA[cValor])/100)*float(despesas[cValor])

print()
print("Soma despesas sem iva", somaSemIVA)
print("Soma das despesas com iva", somaComIVA)
print()