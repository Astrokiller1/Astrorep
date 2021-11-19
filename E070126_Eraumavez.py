casaXa= 1
moedas= 1
Totalmoedas= 0

for casaXa in range (2,65,1):
    moedas *= 2
    Totalmoedas += Totalmoedas + moedas
    print("Casa nº ", casaXa," : ",moedas, "moedas colocadas")

print(Totalmoedas,"Moedas ganhas pelo artesão pelo seu trabalho.")
print("Não sabendo o valor da moeda oferecida nao sabemos o valor real, mas podemos assumir que o rei foi persuadido a pagar mais que o suposto. E que o rei ao ver as torres de moedas que empilhou no tabuleiro com tal surpresa fez cair tudo sobre ele e ficou subterrado seja qual for o valor economico das mesmas.")
