compra_lata = int(input("Digite a quantidade de latas que foi comprada:\n"))
compra_garrafa = int(input("Digite quantas garrafas foram compradas:\n"))
compra_garrafa_maior = int(input("Digite quantas garrafas maiores foram compradas:\n"))
lata = 0.35
garrafa = 0.6
garrafa_maior = 2

conta = compra_lata+compra_garrafa+compra_garrafa_maior
litros = (lata+garrafa+garrafa_maior)+conta

print(conta)
print(litros)
