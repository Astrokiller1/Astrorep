import time
import numpy as np

numNotas = 5
queroSair=''
escolha=''
resposta=''
notas = [0.0 for i in range(numNotas)]
media=0
maximo=0
minimo=20

while (not queroSair):
    print("")
    print("***********************************************",end='\n')
    print("*                                             *",end='\n')
    print("*             Estatistica de notas            *",end='\n')
    print("*                                             *",end='\n')
    print("*      1. Inserção de nota.                   *",end='\n')
    print("*      2. Listar notas.                       *",end='\n')  
    print("*      3. Média das nota.                     *",end='\n')
    print("*      4. Apresentar a nota máxima.           *",end='\n')
    print("*      5. Apresentar a nota minima.           *",end='\n')
    print("*      6. Apagar as notas.                    *",end='\n')
    print("*      7. Sair do programa.                   *",end='\n')
    print("*                                             *",end='\n')
    print("***********************************************",end='\n')
    resposta = input(" -> Escolha uma opção (1-7) : ")
    if ((len(resposta))>0):
        escolha=resposta[0]
    else:
        escolha=0
    if(escolha == "1"): #opçao 1
        print("Insira um conjunto de ", numNotas, "notas : ")
        for cValor in range (0,numNotas,1):
            print("Insira a nota nº ", format(cValor+1), ": ")
            notas[cValor] = float(input())
        input("Prima qq tecla para continuar...")
    elif (escolha=="2"):  #opçao 2
        print("Listagem de notas : ")
        for cValor in range(0,numNotas,1):
            print("Nota ", format(cValor+1)," : ")
            print(format(notas[cValor]))
        input("Prima qq tecla para continuar ...")
    elif(escolha=="3"): #opçao 3
        print("Apresentação da média das notas")
        for cValor in range(0,numNotas,1):
            media += notas[cValor]/numNotas
            print("Média : ", media, ".")
        input("Prima qq tecla para continuar ...")
    elif (escolha=="4"): #opção 4
        print("Apresentar a nota máxima.")
        for cValor in range(0,numNotas,1):
            media +=notas[cValor]/numNotas
            if (cValor==0 or maximo < notas[cValor]):
                maximo = notas[cValor]
            print("A nota maxima é : ", maximo, ".")
            input("Prima qq tecla para continuar ...")
    elif (escolha=="5"): #opção 5
        print("Apresentar a nota minima.")
        for cValor in range(0,numNotas,1):
            media +=notas[cValor]/numNotas
            if (cValor==0 or minimo > notas[cValor]):
                minimo = notas[cValor]
            print("A nota minima é : ", minimo, ".")
            input("Prima qq tecla para continuar ...")
    elif (escolha=="6"): #opção 6
        notas=[0.0 for i in range(numNotas)]
        print("Operação concluida com sucesso.")
        input("Prima qq tecla para continuar")
    elif (escolha== "7"): #opção 7
        resposta = input("Tem a certeza ? (S/N)  ")
        if (resposta[0] =='s' or resposta[0]=='S'):
            queroSair=True
    else:
        print("Opção invalida!")
        input("Prima qq tecla para continuar ...")
print("Obrigado por ter usado o nosso programa!")
input("Prima qq tecla para terminar ...")
print()