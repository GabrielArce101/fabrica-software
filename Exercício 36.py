print("Informe o código do sanduiche e da bebida \n")
total = 0
print("\nCachorro Quente : 100"
      "\nOvo Simples : 101"
      "\nBauru com Ovo : 102"
      "\nHamburger :103"
      "\n"
      "\nBebidas:"
      "\n Refrigerantes : 201"
      "\n Sucos : 202"
      "\n Agua Mineral : 203")

codsand= int(input("\nDigite o código do sanduíche"))
codbeb = int(input("\nDigite o código da bebida"))

match(codsand):
    case 100:
        total = total +11.2
    case 101:
        total = total + 8.3
    case 103:
        total = total +11.5

match(codbeb):
    case 203:
        total = total+6
    case 204:
        total = total + 7.5
    case 205:
        total=total+4.7
