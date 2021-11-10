Nota=float(input("Insira a Nota de 0 a 20 : "))

if (Nota > 8) and (Nota < 12) or (Nota==12):
    print("Satisfaz")
elif (Nota > 4) and (Nota < 8) or (Nota==8):
    print("Insatisfaz")
elif (Nota > 12) and (Nota < 16) or (Nota==16):
    print("Bom")
elif (Nota > 16) and (Nota < 20) or (Nota==20):
    print("Excelente")
elif (Nota > 0) and (Nota < 4) or (Nota==4):
    print("Mau")
elif (Nota == 0):
    print("Não Compareceu")
else: print("Valor de Nota inválido")