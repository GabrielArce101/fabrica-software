#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares
quantidade = 0
numeros=[]
numero=int(input("Digite um número:\n"))
numeros.append(numero)
while quantidade<9:
    numero = int(input("Digite um número:\n"))
    numeros.append(numero)
    quantidade=quantidade+1
    if numero %2==0:
        print("Par")
    else:
        print("Impar")
print(numeros)
