n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite um terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é maior número")

elif n2 > n1 and n2 > n3:
    print(f"{n2} é maior número")

else: 
    print(f"{n3} é maior número")
