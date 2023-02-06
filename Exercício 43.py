um_cente = int(input("Digite a quantidade dessa moeda:\n"))
cinco_cente = int(input("Digite a quantidade dessa moeda:\n"))
dez_cente = int(input("Digite a quntidade dessa moeda:\n"))
vinte_e_cinco_cente = int(input("Digite a quantidade dessa moeda:\n"))
cinquenta_cent = int(input("Digite a quantidade dessa moeda:\n"))
um_real = int(input("Digite a quantidade dessa moeda:\n"))

economizou = um_cente+cinco_cente+dez_cente+vinte_e_cinco_cente+cinquenta_cent
total = economizou/100
total_em_reais = total+um_real


print(total_em_reais)
