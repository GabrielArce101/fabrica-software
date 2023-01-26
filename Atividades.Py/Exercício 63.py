condition = True

soma=0
numero=[]

while condition:
    num=int(input('Digite o numero: '))
    if num != 0:
        soma= soma+num
        numero.append(num)
    else:
        break

print('Soma: ', soma)
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))

