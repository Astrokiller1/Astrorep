import numpy as np
import time



NUMMESAS=7
LIVRE=0
RESERVADA=1
OCUPADA=2
queroSair=False
escolha="\0"

mesas=np.zeros(NUMMESAS)


while not queroSair:
    print("")
    print("")
    print("***********************************")
    print("*                                 *")
    print("*         Rest Guest              *")
    print("*                                 *")
    print("*      1. Listar mesas.           *")
    print("*      2. Reservar mesa.          *")
    print("*      3. Ocupar mesa.            *")
    print("*      4. Libertar mesa.          *")
    print("*      5. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    resposta = input(" -> Escolha uma opção (1-5) : ")
    if (len(resposta)>0):
        escolha = resposta[0]
    else:
        escolha=0
    
    if (escolha=='1'):
        print("Listagem de mesas : ")
        for cmesa in range(0,NUMMESAS,1):
            print(" -> Mesa:",(cmesa+1)," : ")
            if (mesas[cmesa] == LIVRE):
                print("livre.")
            elif (mesas[cmesa]==RESERVADA):
                print(" reservada.")
            else:
                print(" ocupada.")
        input("Prima qq tecla ...")
    elif (escolha=='2'):
        print("Qual é a mesa a reservar (1-",NUMMESAS,") ??")
        nummesa = int(input())
        mesas[nummesa-1]=RESERVADA
        print("Mesa reservada com sucesso!")
        input("Prima qq tecla...")
    elif(escolha =='3'):
        print("Qual é a mesa a ocupar (1-",NUMMESAS,") ??")
        nummesa = int(input())
        mesas[nummesa-1]=OCUPADA
        print("Mesa ocupada com sucesso!")
        input("Prima qq tecla ...")
    elif (escolha=='4'):
        print("Qual é a mesa a libertar (1-",NUMMESAS,") ??")
        nummesa =int(input())
        mesas[nummesa-1]=LIVRE
        print("Mesa libertada com sucesso!")
        input("Prima qq tecla para continuar ...")
    elif (escolha =='5'):
        resposta = input("tem a certeza (S/N) ? ")
        if(resposta[0]=='s' or resposta[0]=='S'):
            queroSair= True
    else:
        print("Opção invalida!")
        input("Prima qq tecla ...")
print("Obrigado por ter usado o nosso programa")
print()