num=int(input("Digite um número:\n"))
impar=0
par=0
while num !=-999:
    if num %2==1:
        impar +=1
    if num%2==0:
        par+=1
    num = int(input("Digite um número:\n"))
print(f"A quantidade de números impares foi de:\n{impar}")
print(f"A quantidade de números pares foi de:\n{par}")
