import numpy as np
import time

NUMANDARES = 3
NUMQUARTOSPORANDAR = 5 
LIVRE =0
RESERVADO =1
OCUPADO =2
queroSair=False
escolha ='\0'

quartos = [[LIVRE for i in range (NUMQUARTOSPORANDAR)]
for j in range(NUMANDARES)]

while (not queroSair):
    print("")
    print("")
    print("***********************************")
    print("*                                 *")
    print("*         Pensao Meireles         *")
    print("*                                 *")
    print("*      1. Listar quartos.         *")
    print("*      2. Reservar quarto.        *")
    print("*      3. Ocupar quarto.          *")
    print("*      4. Libertar quarto.        *")
    print("*      5. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    resposta = input (" -> Escolha uma opção (1-5) : ")
    if (len(resposta)>0):
        escolha = resposta[0]
    else:
        escolha =0
    
    if(escolha =='1'):
       print("Listagem de quartos : ")
       for cAndar in range(0,NUMANDARES,1):
           print("Andar",(cAndar+1)," : ")
           for cQuarto in range (0,NUMQUARTOSPORANDAR,1):
                print(" -> Quarto",(cQuarto+1)," : ")
                if(quartos[cAndar][cQuarto]==LIVRE):
                   print("Livre.")
                elif (quartos[cAndar][cQuarto] ==RESERVADO):
                    print("reservado.")
                else:
                    print("ocupado.")
                input("Prima qq tecla ...")
    elif (escolha=='2'):
        print("Qual é o andar a selecionar (1-",NUMANDARES,")? ")
        numAndar =int(input())
        print("Nesse andar, qual é o quarto a reservar (1-",NUMQUARTOSPORANDAR,")? ")
        numQuarto = int(input())
        quartos[numAndar-1][numQuarto-1] =RESERVADO
        print("Quarto reservado com sucesso!")
        input("Prima qq tecla ...")
    elif (escolha == '3'):
        print("Qual é o andar a selecionar (1 -",NUMANDARES,")? ")
        numAndar = int(input())
        print("Nesse andar, qual é o quarto a ocupar (1-",NUMQUARTOSPORANDAR,")? ")
        numQuarto=int(input())
        quartos[numAndar-1][numQuarto-1]=OCUPADO
        print("Quarto ocupado com sucesso!")
        input("Prima qq tecla ...")
    elif (escolha =='4'):
        print("Qual o andar a selecionar (1-",NUMANDARES,") ? ")
        numAndar =int(input())
        print("Nesse andar, qual é o quarto a libertar (1-",NUMQUARTOSPORANDAR,")? ")
        numQuarto=int(input())
        quartos[numAndar-1][numQuarto-1]=LIVRE
        print("Quarto libertado com sucesso!")
        input("Prima qq tecla ...")
    elif (escolha =='5'):
        resposta = input("tem a certeza (S/N)? ")
        if (resposta[0]=='s' or resposta[0]=='S'):
            queroSair = True
    else:
        print("Opção inválida!")
        input("Prima qq tecla para continuar ...")
print("Obrigado por usar o nosso software")
print()