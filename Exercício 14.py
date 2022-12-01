num = float(input("digite o numero da conta\n"))
saldo: float = float(input("digite o saldo\n"))
debito = float(input("digite o valor a ser debitado\n"))
credito = float(input("digite o valor de seu crédito\n"))

saldo_atual = (saldo-debito+credito)

print("saldo atual\n",saldo_atual)

if saldo_atual >=0:
    print(f"o saldo de sua conta é positivo")
else:
    print(f"o saldo de sua conta está negativo")
