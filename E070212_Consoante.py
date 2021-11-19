letra=str()
contador=1
consoante=int()

while contador<=10:
    print("Insira o caracter para estudo nº", contador ," : ")
    letra=input()
    contador+=1
    letra=letra.lower
    if letra!='a' or letra!='e'or letra!='o' or letra!='i' or letra!='u':
        consoante+=1
print("O numero de Consoantes apresentadas é : ",  consoante,".")