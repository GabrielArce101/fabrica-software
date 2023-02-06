nome = input("Digite seu nome:\n")
sexo = input("Digite seu sexo M ou F:\n")
estado_civil = input("Digite C para casado e S para solteiro:\n").upper()

if sexo == "F" and estado_civil == "C":
    tempo_casado = input("Digite o tempo em que você está casado(a):\n")
    print(tempo_casado)


print(nome)
print(sexo)
print(estado_civil)

