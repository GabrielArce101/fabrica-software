salario=int(input("Digite o valor do salário\n"))
valor_do_financiamento=int(input("Digite o valor do financiamento:\n"))
if valor_do_financiamento<=5*salario:
    print("Financiamento concedido")
else:
    print("Financiamento negado")
