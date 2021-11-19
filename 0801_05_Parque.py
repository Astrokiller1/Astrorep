# 0. Bibliotecas
import sys   # Biblioteca entradas/saídas do sistema
import os    # Biblioteca das funções/comandos do sistema operativo
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
#pip3 install numpy
import numpy as np

# 1. Dados
NUMLUGARES = 7
LIVRE = 0
OCUPADO = 1

queroSair = False
escolha='\0'


# Declaração e Inicialização do vetor
# lugares= np.zeros(NUMLUGARES)
lugares = [LIVRE for i in range(NUMLUGARES)]


while (not queroSair):
# 2. Algoritmo
    # 2.1 Apresentar o menu
    system('cls') # Limpa o ecrã
    print("")
    print("***********************************")
    print("*                                 *")
    print("*             Parque Gest         *")
    print("*                                 *")
    print("*      1. Listar lugares.         *")
    print("*      2. Marcar lugar.           *")
    print("*      3. Libertar lugar.         *")
    print("*      4. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    # 2.2 Pedir uma escolha ao utilizador

    resposta = input(" -> Escolha uma opção (1-4): "); # 1 ENTER
    if (len(resposta) > 0):   # Evita "out of index error"
       escolha = resposta[0]
    else:
       escolha = 0    

    # 2.3 Processa escolha
    if (escolha == '1'):
        print("Listagem de Lugares:")
        for cLugar in range(0,NUMLUGARES,1):
            print(" -> Lugar: ",(cLugar+1),": ", end =" ") 
            if (lugares[cLugar] == LIVRE):
                print(" livre.")
            else: 
                print(" ocupado.")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '2'):  
        print("Qual é o lugar a ocupar (1 -",NUMLUGARES,")? ",end =" ")
        numLugar = int(input())
        lugares[numLugar-1]=OCUPADO
        print("Lugar ocupado com sucesso!")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '3'):  
        print("Qual é o lugar a libertar (1 -",NUMLUGARES,")? ",end =" ")
        numLugar = int(input())
        lugares[numLugar-1]=LIVRE
        print("Lugar libertado com sucesso!")
        input("Prima qq tecla para continuar ...")
    elif (escolha == '4'):  
        resposta = input("Tem a certeza (S/N)? ")
        if (resposta[0] =='s' or resposta[0] =='S'):
            queroSair = True
        elif (resposta[0] =='n' or resposta[0] =='N'):
            queroSair = False
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")        


# 2.5 Despedida
print("Obrigado por ter usado o nosso programa!")
input("Prima qq tecla para continuar ...") 
print()  