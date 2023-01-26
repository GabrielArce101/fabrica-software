num1=int(input("digite um numero--> \n"))
num2=int(input("digite outro numero-->\n "))

while num2<num1:
    num1=int(input("digite um numero-->\n"))
    num2=int(input("digite outro numero-->\n "))
else:
    for i in range(num1,num2,1):
        print(i)
