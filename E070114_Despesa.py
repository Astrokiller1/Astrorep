import sys
import math

despesa= 0
iva= float
tDespesas=0
valorFinal=0
valorCiva=0



for contador in range(0,255,1):
    print("Insira as suas depesas : ")
    despesa=input()
    tDespesas += float(despesa)
    print("Qual o valor do IVA ? ")
    iva=input()
    valorCiva += ( float(iva) * float(despesa))
    print("Quer Inserir outra despesa ? (S/N) ")
    resposta=input()
    if (resposta =='n') or (resposta =='N'):
        break

print("Valor sem iva a gastar",tDespesas)

print("Valor a gastar", valorCiva + tDespesas)