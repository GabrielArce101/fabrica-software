quantidade=0
soma=0
numeros_digitados=[]
numeros=int(input("Digite um número:\n"))
while quantidade<=7:
    numeros = int(input("Digite um número:\n"))
    soma=numeros+numeros
    numeros_digitados.append(numeros)
    quantidade=quantidade+1
    print(numeros_digitados)
    print(soma)
    if quantidade==5:
        break
