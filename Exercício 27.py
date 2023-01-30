alunos = 0
total_de_mulheres = 0
total_de_homens = 0
bons = 0
porcentagem = 0

while alunos <50:
    sexo = input("Digite o sexo:\n")
    altura = float(input("Digite a altura:\n"))
    status = int(input("Digite o status:\n"))

    if(sexo == "F" and altura >1.7):
        total_de_homens = total_de_mulheres+1
    else:
        total_de_homens = total_de_homens+1

    if(sexo == "M" and status == 1):
        bons = bons + 1
        porcentagem = porcentagem * 100 / total_de_homens

        aluno = alunos + 1

print("Total de mulheres altas:\n",total_de_mulheres)
print("Ttotal de mulheres:\n",total_de_homens
