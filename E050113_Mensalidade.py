Sub_Refei = float(input("Insira Subsidio de Refeição:"))
Sal_H = float(input("Insira o Salario por Hora:"))
Sub_Trans = float(input("Insira o Subsidio de Transporte:"))
Hor_Trab = float(input("Insira Horas em Serviço Efectivo por Dia:"))
Dias_Prod = float(input("Insira o Numero de Dias Produtivos por Mês:"))

Mensalidade = (Sub_Trans + Sub_Refei + (Sal_H*Hor_Trab))*Dias_Prod

print("O Valor Expectado por Mês Será:",Mensalidade)