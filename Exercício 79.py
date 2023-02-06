#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
Alunos = 5
Notas = 4
medias = []
media_sete = 0
for i in range(Alunos):
    media = 0
    for j in range(Notas):
        media += float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
    media /= Notas
    medias.append(media)
    if media >= 7:
        media_sete += 1

print("\nA média dos alunos foi:")
for i in range(Alunos):
    print(f"Aluno {i+1}: {medias[i]}")

print(f"\n{media_sete} alunos tiveram média maior ou igual a 7.")
