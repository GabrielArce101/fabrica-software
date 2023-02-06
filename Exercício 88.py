pagamento=0
troco=0
while pagamento==0:
    print("1- Café normal\n 2- Café expresso\n 3- Capuccino\n 4- Mocaccino\n")
    tipos_de_cafe = int(input("informe o tipo do café:\n"))
    pagamento=(float(input("Informe o valor do pagamento:\n")))
    if tipos_de_cafe==1:
        nome="Café normal"
        print("O valor do café é R$1,05")
    elif tipos_de_cafe==2:
        nome="Café expresso"
        print("O valor do café é R$1,52")
    elif tipos_de_cafe==3:
        nome="Capuccino"
        print("O valor do café é R$2,17")
    elif tipos_de_cafe==4:
        nome="Mocaccino"
        print("O valor do café é R$2,36")


troco=pagamento
print(f'O valor do seu troco é :{troco}')
