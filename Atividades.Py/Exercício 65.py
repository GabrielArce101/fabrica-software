divida=int(input("Digite o valor de sua divida:\n"))
parcelas=int(input("Em quantas vezes você pretende parcelar sua divida?\n"))
juros=0

if parcelas==1:
    juros=divida+0.0
    total_parcelas=juros/1
if parcelas==3:
    juros=divida+((divida*10)/100)
    total_parcelas=juros/3
if parcelas==6:
        juros=divida+((divida*15)/100)
        total_parcelas=juros/6
if parcelas==9:
    juros=divida+((divida*20)/100)
    total_parcelas=juros/9
if parcelas==12:
    juros=divida+((divida*25)/100)
    total_parcelas=juros/12
print("="*50)
print(f"R${divida}       {parcelas}         R${juros}      R${total_parcelas}")