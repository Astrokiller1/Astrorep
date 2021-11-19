import sys
import math

nota= 0.0
numAlunos=int(input("Insira o numero de alunos pertencentes a turma em estudo : "))
positiva= 0
positivaPercent= 0

for contador in range(1,(numAlunos+1),1):
    nota=input("Insira nota referente ao aluno nº " + format(contador) + " : ")
    if (float(nota) > 9.4) and (float(nota) <= 20):
        print("Aluno aprovado, nota positiva")
        positiva += 1
    elif(float(nota)<9.5) and (float(nota)>=0): 
        print("Nota negativa, aluno reprovado ")
    else:
        print("Valor inválido") 
        break

positivaPercent= (positiva/numAlunos)*100
print("A percentagem de alunos Aprovados é : ", round(positivaPercent,1), "%.")
