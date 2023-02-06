print("\n Cidade 10  :  1"
      "\n Cidade 20  :  2"
      "\n Cidade 30  :  3"
      "\n Cidade 40  :  4"
      "\n Cidade 50  :  5")
codcidade= int(input("Selecione a cidade:\n"))

cidade10=10000
cidade20=15000
cidade30=1700
cidade40=1000
cidade50=2500


if codcidade==1:
      print(f"Existem exatamente {cidade10} carros nessa cidade")
if codcidade==2:
      print(f"Existem exatamente {cidade20} carros nessa cidade")
if codcidade==3:
      print(f"Existem exatamente {cidade30} carros nessa cidade")
if codcidade==4:
      print(f"Existem exatamente {cidade40} carros nessa cidade")
if codcidade==5:
      print(f"Existem exatamente {cidade50} carros nessa cidade")
print("⭐"*50)

print("A média de veículos entres essas cidades é de:\n")
media=(cidade10+cidade20+cidade30+cidade40+cidade50)/5
print(media)
print("⭐"*50)

indice= codcidade-codcidade
print(indice)
