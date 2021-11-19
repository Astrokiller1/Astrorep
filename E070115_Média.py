import sys
import math

nota= 0
media = 0.0

for contador in range(1,8,1):
    nota=float(input("Insira nota referente a trabalho " + format(contador) + " : "))
    media += float(nota)/7

print("A  média das suas notas finais foi : ", round(media,2))