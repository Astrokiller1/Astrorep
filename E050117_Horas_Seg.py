Hora = float(input("Insira as Horas Registadas:"))
Min = float(input("Insira os Minutos Registados:"))
Seg = float(input("Insira os Segundos Registados:"))

Segundos= Hora*3600 + Min*60 + Seg

print("O Tempo do Atleta em Segundos é:",Segundos)