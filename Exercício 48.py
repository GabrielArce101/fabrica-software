produto = int(input("Digite o valor do produto:\n"))
pagamento = print("1 Dinehiro ou Pix \n 2 Cartão de crédito\n 3 parcelado")

if pagamento == 1:
    nome = "Dinheiro ou Pix"
    valor = produto - 0.1

if pagamento == 2:
    nome = "Cartão de crédito"
    valor = produto - 0.05

if pagamento == 3:
    nome = "Parcelado"
    valor = produto/2

else:
    valor = produto/3

    print(valor)
