peso =  50
multa_por_excesso = 4

if (peso >= 50):
    peso = (int(input("Digite o peso do peixe\n")))
else:
    Total_a_pagar = peso + multa_por_excesso

print("Total da multa:\n",Total_a_pagar)
