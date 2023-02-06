encontrado=0
numeros = []
for c in range(3):
    numeros.append(int(input(f'Digite um número{c+1}: ')))
num = int(input("Numero para verificar: "))
for c in range(len(numeros)):
    if num == numeros:
        print("Encontrou")
    else:
        print("NÃO Encontrou")
