numCaracteres=10
numvog=0
letra= str('/0')

print()
for contador in range(0, numCaracteres,1):
    print("Insira um caracter seguido" + " de ENTER ("+format(contador+1,"2d")+"): ", end="") 
    letra=input()
    if (letra.isalpha()):
        print("Inseriu um caractere alfabético!!")
        letra = letra.lower()
        if (letra=='a' or letra == 'e' or  letra=='i' or letra=='o' or letra=='u') :
            numvog +=1
print("Número de vogais inseridas: " +format(numvog)+".")
print()