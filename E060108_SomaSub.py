num1=float(input("Insira o Primeiro Valor : "))
num2=float(input("Insira o Segundo Valor : "))
op= input("Insira a Operação a Realizar : ")

if (op=='+'):
    print(num1 + num2)
elif (op=='-'):
    print(num1 - num2)
else: print("Operação inválida, tente novamente")
