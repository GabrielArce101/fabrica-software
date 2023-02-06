                                                           # Variaveis compostas
                        #As variaveis são divididas por indices de 0 a 4, onde 0 é o primeiro indice e assim por diante.
                                                                                                                         #        0, 1, 2
                                                                                                                        #notas = [10,9,6]
                                                                                                                        #print(notas[2])

Alunos = ["Alessandra", "Joceyr", "Thiago", "Vitor","Márcia","Paulo"]
print(Alunos)                                                                                                           #Nesse caso não foi definido qual dos nomes eu quero "puxar"

# print(Alunos[0:2])                                                                                                    #Nesse casso será mostrado os nomes nas posições 0 e 2

for al in range(0,len(Alunos)):
    print(f'Os alunos da Fábrica são {al}')                                                                             #Este exemplo mostrará as posições dos alunos em seus indices.
print("➖"*100)
for al in range(0,len(Alunos)):
    print(f'Os alunos da Fábrica são {Alunos[al]}')                                                                     #Contará os alunos entre os indices 0 ao 4
print('➖'*100)

for al in range(0,len(Alunos)):
    print(f'Os alunos da Fábrica são {Alunos[al]} e estão na posição {al} da tupla')                                    #Mostra sua posição dentro da tupla
print('➖'*100)

print("De tras pra frente")
for al in range(-1,-7,-1):
    print(f'Os alunos da Fábrica são {Alunos[al]}')                                                                     #Mostra sua posição dentro da tupla
print('➖'*100)
