codprato= int(input("Selecione um prato:\n"))
confirmacao= str(input("Selecione Y ou N se deseja adicionar gorjeta:\n")).upper()
if confirmacao == "Y":
      total = 0.1+codprato
elif confirmacao == "N":
      total = total+codprato

prato1 = 15.00
prato2 = 30.00
prato3 = 5.005
prato4 = 10
prato5 = 2.50
gorjeta = 0.10

match(codprato):
      case 1:
            total = total+15.00
      case 2:
            total = total+30
      case 3:
            total = total+5
      case 4:
            total = total+10
      case 5:
            total=total+2.50
print(total)
