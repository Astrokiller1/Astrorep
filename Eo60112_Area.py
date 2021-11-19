Escolha=str(input("Escolha a area que deve Calcular : "))

Largura = float(input("Insira a largura do Sólido : "))
Comprimento = float(input("Insira a comprimento do Solido : "))

Raio = int(input("Insira o Raio do Circulo : "))
Pi= float('3.1415')


Basetri = float(input("Insira a Dimensão da Base do Triangulo : "))
Alturatri = float(input("Insira a Dimensão da Altura do Triangulo : "))

AreaSolido = (Largura * Comprimento)
AreaTri= Basetri * Alturatri / 2
ACirc = Pi*Raio**2

if (Escolha== "Quadrado"):
    print("Area do Solido : ", AreaSolido)
elif (Escolha== "Circulo"):
    print('Area do Circulo : ', ACirc)
elif (Escolha== "Triangulo"):
    print('Area do Triangulo é : ',AreaTri)
else: print("Escolha uma das opções válidas (Quadrado;Circulo;Triangulo)")
