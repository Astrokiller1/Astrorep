import sys
import math

nota= 0
media = 0.0
numTrab= int(input("Quantos Trabalhos realizou este semestre ?"))

for contador in range(1,(numTrab+1),1):
    nota=float(input("Insira nota referente a trabalho " + format(contador) + " : "))
    media += float(nota)/numTrab

print("A  média das suas notas finais foi : ", round(media,2))