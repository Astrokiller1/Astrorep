import sys
import math

despesa= 0
numdespesas=0
iva= float
tDespesas=0
valorFinal=0
valorCiva=0
contador=numdespesas-1


while contador < numdespesas:
    print("Insira as suas depesas : ")
    despesa=input()
    numdespesas+=1
    tDespesas += float(despesa)
    print("Qual o valor do IVA em numero decimal ? ")
    iva=input()
    valorCiva += ( float(iva) * float(despesa))
    print("Quer Inserir outra despesa ? (S/N) ")
    numdespesas+=1
    resposta=input()
    if (resposta =='n') or (resposta =='N'):
        break

print("Valor sem iva : ",tDespesas)

print("Valor a gastar : ", valorCiva + tDespesas)