soma = 0
mult = 1
media = 5
for c in range(0,5):
    num= float(input("Digite um número:\n"))
    soma = soma+num
    mult= mult*num


print(f'A soma dos números digitados foram:\n {soma}')
print(f'A multiplicação desses números é de:\n{mult}')
print(f'A média dos números digitados foram de:\n{(soma)/5}')
