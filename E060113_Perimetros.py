Escolha=str(input("Escolha a area que deve Calcular : "))

Largura = float(input("Insira a largura do Rectangulo:"))
Comprimento = float(input("Insira a comprimento do Rectangulo:"))

Perimetro = (2*Largura+ 2*Comprimento)


Raio = int(input("Insira o Raio do Circunferencia:"))
Pi= float('3.1415')

PeriCirc= 2 * Pi * Raio



Lado1 = float(input("Insira a Dimensao do Lado1 do Triangulo:"))
Lado2 = float(input("Insira a Dimensao do Lado2 do Triangulo:"))
Lado3 = float(input("Insira a Dimensao do Lado3 do Triangulo:"))

PeriTri = Lado1 + Lado2 + Lado3



if (Escolha== "Quadrado"):
    print('Perimetro do Rectangulo/Quadrado : ',Perimetro)
elif (Escolha== "Circulo"):
    print('Perimetro do Circunferencia : ',PeriCirc)
elif (Escolha== "Triangulo"):
    print("Perimetro do Triangulo é : ",PeriTri)
else: print("Escolha uma das opções válidas (Quadrado;Circulo;Triangulo)")