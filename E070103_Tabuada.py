tabuada= int(input("Escolha a Tabuada a apresentar de 1 a 10 : "))
contador= 0

for contador in range(1,11,1):
    print (contador, '*', tabuada,'=',contador*tabuada)
