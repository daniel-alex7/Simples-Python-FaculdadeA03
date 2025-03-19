n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro inteiro: "))

if n1 >= n2 and n1 >= n3:
    print(n1, "Maior número")
elif n2 >= n1 and n2 >= n3:
    print(n2, "Maior número")
else:
    print(n3, "Maior número")