populacaoA=80000
populacaoB=200000
taxa_de_crescimentoA= ((populacaoA*3)/100)
taxa_de_crescimentoB=((populacaoB*1.5)/100)
tempo_necessario = 0

while taxa_de_crescimentoA < taxa_de_crescimentoB:
    tempo_necessario = taxa_de_crescimentoA<taxa_de_crescimentoB *(tempo_necessario+1)

print(taxa_de_crescimentoA)
print(taxa_de_crescimentoB)
print(tempo_necessario)