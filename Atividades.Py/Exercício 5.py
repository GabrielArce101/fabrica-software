nome = input("digite seu nome: \n")
disciplina = input("digite o nome da disciplina: \n")
prova1 = float(input("digite a nota da prova: \n"))
prova2 = float(input("digite a nota da prova: \n"))
prova3 = float(input("digite a nota da prova: \n"))
media= (prova1+prova2+prova3)/3
if(media>= 6):
    print(f"As notas foram:{prova1},{prova2},{prova3} Media do "
          f"aluno {nome} foi {media:.1f}, foi o suficiente para passar.")

else:
    print(f"As notas foram: {prova1}, {prova2}, {prova3} Media"
    f"aluno {nome} foi {media:.1f}, foi insuficiente para passar ")

print("nome: ",nome)
print("disciplina: ",disciplina)
print("prova1: ",prova1)
print("prova2 ",prova2)
print("prova3 ",prova3)
print("media",media)
