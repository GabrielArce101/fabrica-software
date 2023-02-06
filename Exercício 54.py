num= int(input("Digite um número:\n"))
maior=num
menor=num
for i in range(1,20):
    num = int(input("Digite outro número:\n"))
    if num < menor:
        menor=num
    if num > maior:
        maior = num

print(f"O mairo número foi:\n {maior}")
print(f"O menor número foi:\n{menor}")
