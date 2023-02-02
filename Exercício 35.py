print("1- File Duplo\n 2- Alcatra\n 3- Picanha\n\n")
tipo = int(input("Digite o tipo: "))
quantidade = int(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartao Tabajara? 1/ SIM - 2/ NAO: "))

if tipo == 1:
    nome = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 34.90
    else:
        preco = quantidade * 35.80

if tipo == 2:
    nome = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 44.90
    else:
        preco = quantidade * 46.80

if tipo == 3:
    nome = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 66.90
    else:
        preco = quantidade * 67.80

if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) / 100)
    total = preco - desconto
else:
    r = "NAO"
    total = preco

print("\n***************************CUPOM FISCAL**************************************")
print("* Carne.......................................................... %s " %nome)
print("* Quantidade..................................................... %d KG " %quantidade)
print("* Preço......................................................... %2.f R$ " %preco)
print("* Cartao Tabajara................................................ %s " %r)
print("* Total com desconto............................................ %2.f R$ " %total)
print("******************************************************************************")
