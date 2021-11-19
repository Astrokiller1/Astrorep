num1=float(input("Insira o Primeiro Valor : "))
num2=float(input("Insira o Segundo Valor : "))
op= input("Insira a Operação a Realizar : ")
print("Relembre que a raiz será equivalente ao inverso da potencia, ou seja num1**1/num2")

if (op=='+'):
    print(num1 + num2)
elif (op=='-'):
    print(num1 - num2)
elif (op=='*'):
    print(num1 * num2)
elif (op=='/'):
    print(num1 / num2)
elif (op=='**'):
    print(num1**num2)
elif (op=='**/'):
    print(num1**(1/num2))
else: print("Operação inválida, tente novamente")
