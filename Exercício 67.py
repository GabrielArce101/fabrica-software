usuario = input("Nome de usuário:\n")
senha = input("Digite sua senha:\n")

while senha==usuario:
    print("A senha não poder a mesma que seu nome de usuario.\n")
    usuario = input("Nome de usuário:\n")
    senha = input("Digite sua senha:\n")

else:
    print("Registro feito com sucesso👍😎\n"
