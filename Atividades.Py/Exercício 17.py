salario = float(input("digite o valor do salario\n"))
if salario <= 280:
    salario_atual = salario+(salario*0.2)
    print(f"O salario é de {salario_atual}")

elif salario > 280 and salario <=700:
    salario_atual = salario+(salario*0.15)
    print(f"O auento do salario foi de 15%, seu novo salario é de  {salario_atual}")

if salario > 700 and salario <=1500:
    salario_atual = salario+(salario*0.1)
    print(f"O foi de 10%, seu novo salario é de  {salario_atual}")









