import numpy as np
from time import sleep

numlugares=70
NUMlinhas = 7
NUMcolunaPORlinha = 10 
LIVRE =0
RESERVADO =1
OCUPADO =2
queroSair=False
escolha ='\0'



lugares = [[LIVRE for i in range (NUMcolunaPORlinha)]
for j in range(NUMlinhas)]



while not queroSair:
    print("")
    print("")
    print("***********************************")
    print("*                                 *")
    print("*         Cinemas SON             *")
    print("*                                 *")
    print("*      1. Listar lugares.         *")
    print("*      2. Reservar lugar.         *")
    print("*      3. Ocupar lugar.           *")
    print("*      4. Libertar lugar.         *")
    print("*      5. Fim do Filme.           *")
    print("*      6. Sair do programa        *")
    print("*                                 *")
    print("*                                 *")
    print("***********************************")
    print()

    resposta = input (" -> Escolha uma opção (1-6) : ")
    if (len(resposta)>0):
        escolha = resposta[0]
    else:
        escolha =0
    
    if(escolha =='1'):
       print("Listagem de lugares : ")
       for cLinha in range(0,NUMlinhas,1):
           print("Linha",(cLinha+1)," : ")
           for cColuna in range (0,NUMcolunaPORlinha,1):
                print(" -> Lugar",(cColuna+1)," : ")
                if(lugares[cLinha][cColuna]==LIVRE):
                   print("Livre.")
                elif (lugares[cLinha][cColuna] ==RESERVADO):
                    print("reservado.")
                else:
                    print("ocupado.")
                print(LIVRE)
                input("Prima qq tecla ...")
    elif (escolha=='2'):
        print("Qual é a linha que prefere de : (1-",NUMlinhas,")? ")
        numlinha =int(input())
        print("Nessa Linha, qual é o Lugar a reservar (1-",NUMcolunaPORlinha,")? ")
        numcoluna = int(input())
        lugares[numlinha-1][numcoluna-1] =RESERVADO
        print("Lugar reservado com sucesso!")
        input("Prima qq tecla ...")
    elif (escolha == '3'):
        print("Qual é a linha que prefere de : (1 -",NUMlinhas,")? ")
        numlinha = int(input())
        print("Nessa linha qual o lugar que pretende : (1-",NUMcolunaPORlinha,")? ")
        numcoluna=int(input())
        lugares[numlinha-1][numcoluna-1]=OCUPADO
        print("Lugar ocupado com sucesso!")
        input("Prima qq tecla ...")
    elif (escolha =='4'):
        print("Qual a linha a selecionar (1-",NUMlinhas,") ? ")
        numlinha =int(input())
        print("Nesse linha, qual é a coluna a libertar (1-",NUMcolunaPORlinha,")? ")
        numcoluna=int(input())
        lugares[numlinha-1][numcoluna-1]=LIVRE
        print("Lugar Desocupado!")
        input("Prima qq tecla ...")
    elif (escolha=='5'):
        resposta=input("Por favor confirme que a sessão terminou!! : ")
        if (resposta[0]=='s' or resposta[0]=='S'):
            lugares[numlinha-7][numcoluna-10]=LIVRE
    elif (escolha =='6'):
        resposta = input("tem a certeza (S/N)? ")
        if (resposta[0]=='s' or resposta[0]=='S'):
            queroSair = True
