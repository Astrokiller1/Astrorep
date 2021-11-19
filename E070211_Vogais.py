letra=str()
contador=1
vogal=int()

while contador<=10:
    print("Insira o caracter para estudo nº", contador ," : ")
    letra=input()
    contador+=1
    letra=letra.lower
    if letra=='a' or letra=='e'or letra=='o' or letra=='i' or letra=='u':
        vogal+=1
print("O numero de Vogais apresentadas é : ",  vogal,".")