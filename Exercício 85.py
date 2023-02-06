professor1=int(input("Digite a quantidade de horas do professor 1:\n"))
valor_da_hora1=int(input("Digite o valor da hora:\n"))

professor2=int(input("Digite a quantidade de horas do professor 2:\n"))
valor_da_hora2=int(input("Digite o valor da hora:\n"))

salario_professor1=professor1*valor_da_hora1
salario_professor2=professor2*valor_da_hora2

if salario_professor1>salario_professor2:
    print("O professor 1 recebe mais que o professor 2")
else:
    print("O professor 2 recebe mais que o professor 1")
