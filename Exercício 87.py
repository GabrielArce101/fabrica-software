#Crie um algoritmo para uma empresa de transportes que, a partir do peso de uma encomenda fornecida pelo usuário, calcule o preço da remessa conforme a seguinte tabela:
encomenda=float(input("Digite o peso da encomenda:\n"))
if encomenda<=500:
    print("O valor da encomenda será de R$ 1,10")

elif encomenda<2000>500:
    print("O valor da encomenda será de R$ 2,20")

elif encomenda<=10000>=2000:
    print("O valor da encomenda será de R$ 3,70")

elif encomenda>10000:
    print(f'O preço da encomenda será de R$ 5,00 + R$ 3,80/kg pelo peso que ultrapassar 10kg ')
