litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ").upper()
preco = 0

if combustivel == "A":
    combustivel = "alcool"
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100

    else:
        preco -= 1.9 * litros * 5 / 100

elif combustivel == "G":
    combustivel = "gasolina"
    preco = litros * 2.5

    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100

    else:
        preco -= 2.5 * litros * 6 / 100

print(combustivel)
print(preco)
