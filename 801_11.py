
import numpy as np
from time import sleep

NUMBANCADAS=4
NUMFILAS = 6
NUMLUGARESPORFILA=7
LIVRE=0
RESERVADO =1
OCUPADO=2
queroSair=False
escolha='\0'

lugares = [
    [
        [LIVRE 
        for i in range(NUMLUGARESPORFILA)]
            for j in range(NUMFILAS)]
                for k in range(NUMBANCADAS)]
while (not queroSair):
    print()
    print("")
    print("")
    print("**********************************")
    print("*                                *")
    print("*            Estadio             *")
    print("*                                *")
    print("*      1. Listar lugares.        *")
    print("*      2. Reservar lugar.        *")
    print("*      3. Ocupar lugar.          *")
    print("*      4. Final do Jogo          *")
    print("*      5. Sair do programa       *")
    print("*                                *")
    print("**********************************")
    print()
    resposta = input(" -> Escolha uma opção (1-5): ")
    if (len(resposta) >0):
        escolha = resposta[0]
    else:
        escolha = 0
    if (escolha=='1'):
        print("Listagem de lugares:")
        for cBancada in range(0,NUMBANCADAS,1):
            print("Bancada ", (cBancada+1)," : ")
            for cFila in range(0,NUMFILAS,1):
                print(" ->Fila ",(cFila+1)," : ")
                for cLugar in range(0,NUMLUGARESPORFILA,1):
                    print("-> Lugar ",(cLugar+1)," : ")
                    if (lugares[cBancada][cFila][cLugar]==LIVRE):
                        print("Livre.")
                    elif (lugares[cBancada][cFila][cLugar]==RESERVADO):
                        print("Reservado.")
                    else:
                        print("Ocupado.")
                input("Prima qq tecla para continuar ...")
    elif (escolha =='2'):
        print("Qual é a bancada a selecionar (1-",NUMBANCADAS,") ? ")
        numBancada =int(input())
        print("Qual é a fila a selecionar (1 -",NUMFILAS,") ? ")
        numFila= int(input())
        print("Nessa fila, qual o lugar a reservar (1 -",NUMLUGARESPORFILA,") ? ")
        numLugar= int(input())
        lugares[numBancada-1][numFila-1][numLugar-1]=RESERVADO
        print("Lugar reservado com sucesso !!!")
        input("Prima qq tecla para continuar ...")
    elif (escolha =='3'):
        print("Qual é a bancada a selecionar ? ")
        numBancada =int(input())
        print("Qual é a fila a selecionar (1 -",NUMFILAS,") ? ")
        numFila= int(input())
        print("Nessa fila, qual o lugar a reservar (1 -",NUMLUGARESPORFILA,") ? ")
        numLugar= int(input())
        lugares[numBancada-1][numFila-1][numLugar-1]==OCUPADO
        print("Lugar ocupado com sucesso !!!")
        input("Prima qq tecla para continuar ...")
    elif (escolha=='4'):
        lugares=[[[LIVRE
        for i in range(NUMLUGARESPORFILA)]
        for j in range(NUMFILAS)]
        for k in range(NUMBANCADAS)]
        print("Lugares libertador com sucesso!!")
        input("Prima qq tecla para continuar ...")
    elif (escolha=='5'):
        resposta = input("Tem a certeza (S/N) ? ")
        if (resposta[0] =='s' or resposta[0]=='S'):
            queroSair = True
    else: 
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")
print("Obrigado por usar o nosso programa!")          