import sys
import math

nota= 0
numTrab= int(input("Quantos Trabalhos realizou este semestre ?"))
maximo = 0

for contador in range(1,(numTrab+1),1):
    nota=float(input("Insira nota referente a trabalho " + format(contador) + " : "))
    if (contador==1 or float(nota) > maximo ):
        maximo= float(nota)    

print("A nota maxima das suas notas finais foi : ", maximo)