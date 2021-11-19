import numpy as np
import time

numTaxis = 7
LIVRE = 0
RESERVADO = 1
OCUPADO=2
queroSair =  False
escolha='\0'

taxis = np.zeros(numTaxis)

while not queroSair:
    print("")
    print("")
    print("***********************************")
    print("*                                 *")
    print("*         Central Taxis           *")
    print("*                                 *")
    print("*      1. Listar taxis.           *")
    print("*      2. Reservar taxi.          *")
    print("*      3. Ocupar taxi.            *")
    print("*      4. Libertar taxi.          *")
    print("*      5. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    resposta = input(" -> Escolha uma opção (1-5) : ")
    if (len(resposta)>0):
        escolha =resposta[0]
    else:
        escolha= 0
    if (escolha=="1"):
        print("Listagem de taxis : ")
        for ctaxi in range (0,numTaxis,1):
            print( " -> Taxi : ", (ctaxi+1)," : ")
            if (taxis[ctaxi] ==  LIVRE):
                print(" livre.")
            elif (taxis[ctaxi] == RESERVADO):
                print(" Reservado. ")
            else:
                print(" Ocupado. ")
        input("Prima qq tecla ...")
    elif (escolha=='2'):
        print("Qual é o taxi a reservar (1-", numTaxis, ") ? ")
        numtaxi=int(input())
        taxis[numtaxi-1]=RESERVADO
        print("Taxi reservado com sucesso!!")
        input("Prima qq tecla ...")
    elif(escolha=='3'):
        print("Qual é o taxi a ocupar (1-",numtaxi,") ? ")
        numtaxi=int(input())
        taxis[numtaxi-1]=OCUPADO
        print("Taxi ocupado com sucesso!")
        input("Prima qq tecla ...")
    elif(escolha=='4'):
        print("Qual é o taxi a libertar ?(1-",numtaxi,") ?")
        numtaxi =int(input())
        taxis[numtaxi-1]=LIVRE
        print("Taxi libertado com sucesso!")
        input("Prima qq tecla ...")
    elif (escolha=='5'):
        resposta = input("Tem a certeza que pretende sair ?? (S/N)")
        if (resposta[0] =='s' or resposta[0]=='S'):
            queroSair=True
        elif (resposta[0] =='N' or resposta[0]=='n'):
            queroSair=False
    else:
        print("Opção inválida!!")
        input("Prima qq tecla ...")   
