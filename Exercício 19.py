lado1 = float(input("digite o valor\n"))
lado2 = float(input("digite o valor\n"))
lado3 = float(input("digite o valor\n"))
soma = lado1+lado2+lado3

if lado1 + lado2 > lado3:
    print("esses valores forma um triangulo")
elif lado1 + lado2 < lado3:
    print("esses valores não formam um triangulo")

if lado1 == lado2 == lado3:
    print("Esse trinagulo é equilatero")
elif lado1 == lado2:
    print("Esse triangulo é isósceles")

if lado1 != lado2 != lado3:
    print("Esse triangulo é escaleno")