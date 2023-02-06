print("1- Altair\n 2- Jonas\n 3- Waldisney\n 4- Piripotete\n 5- Nulo\n 6- Branco\n")
presidente = int(input("Digite o seu voto:\n"))
quantidade_Altair = 0
quantidade_Jonas=0
quantidade_Waldisney=0
quantidade_Piripotete=0
quantidade_Nulo=0
quantidade_Branco=0
voto=0
while voto != 10:
    print("1- Altair\n 2- Jonas\n 3- Waldisney\n 4- Piripotete\n 5- Nulo\n 6- Branco\n")
    presidente = int(input("Digite o seu voto:\n"))
    print(quantidade_Jonas,
          quantidade_Altair,
          quantidade_Waldisney,
          quantidade_Piripotete,
          quantidade_Nulo,
          quantidade_Branco)

    if presidente==1:
        voto="Altair"
        quantidade_Altair+=1
        print(quantidade_Jonas,
              quantidade_Altair,
              quantidade_Waldisney,
              quantidade_Piripotete,
              quantidade_Nulo,
              quantidade_Branco)


    if presidente==2:
        voto= "Jonas"
        quantidade_Jonas+=1
        print(quantidade_Jonas,
              quantidade_Altair,
              quantidade_Waldisney,
              quantidade_Piripotete,
              quantidade_Nulo,
              quantidade_Branco)


    if presidente==3:
        quantidade_Waldisney+=1
        print(quantidade_Jonas,
              quantidade_Altair,
              quantidade_Waldisney,
              quantidade_Piripotete,
              quantidade_Nulo,
              quantidade_Branco)

    if presidente==4:
        print(quantidade_Jonas,
              quantidade_Altair,
              quantidade_Waldisney,
              quantidade_Piripotete,
              quantidade_Nulo,
              quantidade_Branco)

        quantidade_Piripotete+=1
    if presidente==5:

        quantidade_Nulo+=1
    if presidente==6:

        quantidade_Nulo+=1

    if quantidade_Nulo or quantidade_Branco or quantidade_Piripotete or quantidade_Waldisney or quantidade_Jonas or quantidade_Altair == 10:
        print("Este candidato foi o ganhador\n")
