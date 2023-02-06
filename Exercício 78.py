#Faça um Programa que leia 20 números inteiros e indique se eles são PAR ou IMPAR. Imprima-os no final.
quantidade = 0
par=[]
impar=[]
numero=int(input("Digite um número:\n"))

while quantidade<9:
    numero = int(input("Digite um número:\n"))
    quantidade=quantidade+1
    if numero %2==0:
        par.append(numero)
    elif numero %2!=0:
        impar.append(numero)


print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')
