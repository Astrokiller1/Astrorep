a= str("int(x [,base])")
b=str("long(x [,base] )")
c=str("float(x)")
d=str("str(x)")
numTenta=3

print("int(x [,base])", 'a')
print("long(x [,base] )",'b')
print("float(x)",'c')
print("str(x)",'d')
print("O numero de tentativas que tem:",numTenta)
x= str(input("Qual a funçao que converte uma variavel para float python? : "))


if (x== 'c'):
    print("Resposta Correta !!")
    numTenta=0
elif (x == 'a') or (x== 'b') or (x== 'd'):
    print("Resposta Errada")
    numTenta -=1
else: 
    print("Resposta inválida!! Deverá escolher entre (a;b;c;d)")
    numTenta -=1

if (numTenta > 0 ) :
    print("int(x [,base])", 'a')
    print("long(x [,base] )",'b')
    print("float(x)",'c')
    print("str(x)",'d')
    print("O numero de tentativas restantes é :",numTenta)
    x= str(input("Qual a funçao que converte uma variavel para float python? : "))
    if (x== 'c'):
        print("Resposta Correta !!")
        numTenta -=2
    elif (x == 'a') or (x== 'b') or (x== 'd'):
        print("Resposta Errada")
        numTenta -=1
    else: 
        print("Resposta inválida!! Deverá escolher entre (a;b;c;d)")
        numTenta -=1
    
if (numTenta > 0):
    print("int(x [,base])", 'a')
    print("long(x [,base] )",'b')
    print("float(x)",'c')
    print("str(x)",'d')
    print("O numero de tentativas restantes é :",numTenta)
    x= str(input("Qual a funçao que converte uma variavel para float python? : "))
    if (x== 'c'):
        print("Resposta Correta !!")
        numTenta -=1
    elif (x == 'a') or (x== 'b') or (x== 'd'):
        print("Resposta Errada")
        numTenta -=1
    else: 
        print("Resposta inválida!! Deverá escolher entre (a;b;c;d)")
        numTenta -=1
else: print("Não tem mais tentativas")