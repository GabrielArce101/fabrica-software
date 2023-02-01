valor_do_saque = int(input("Digite o valor do saque:\n"))

cem = valor_do_saque/100
valor_do_saque = valor_do_saque - (cem*100)

cinquenta =int(valor_do_saque/50)
valor_do_saque = valor_do_saque - (cinquenta*50)

dez = int(valor_do_saque/10)
valor_do_saque = valor_do_saque - (dez*10)

cinco = int(valor_do_saque/5)
valor_do_saque= valor_do_saque - (cinco*5)

print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
