import sys
import math

nota= 0
numTrab= int(input("Quantos Trabalhos realizou este semestre ?"))
minimo = 0

for contador in range(1,(numTrab+1),1):
    nota=input("Insira nota referente a trabalho " + format(contador) + " : ")
    if (contador==1 or float(nota) < minimo ):
        minimo= float(nota)    

print("A nota minima das suas notas finais foi : ", minimo)