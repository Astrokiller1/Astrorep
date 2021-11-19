import sys
import math

nota= 0
numTrab= int(input("Quantos Trabalhos realizou este semestre ?"))
minimo = 0
maximo = 0
media = 0

for contador in range(1,(numTrab+1),1):
    nota=input("Insira nota referente a trabalho " + format(contador) + " : ")
    media += float(nota)/numTrab
    if (contador==1 or float(nota) < minimo ):
        minimo= float(nota)
    if (contador==1 or float(nota) > maximo ):
        maximo= float(nota)
    

print("A nota minima das suas notas finais foi : ", minimo)
print("A nota maxima das suas notas finais foi : ", maximo)
print("A  média das suas notas finais foi : ", round(media,2))