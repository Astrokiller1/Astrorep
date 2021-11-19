tabuada = int(input("Insira a Tabuada desejada de 1 a 10 : "))
contador = 0
resultados= 0


while (contador <11):
    resultados = contador * tabuada
    print(contador, '*', tabuada, '=  ', resultados)
    contador +=1

