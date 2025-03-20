n1 = int(input("Digite um número inteiro A: "))
n2 = int(input("Digite o segundo número inteiro B: "))
n3 = int(input("Digite o terceiro inteiro C: "))

if n1 >= n2 and n1 >= n3:
    print(n1, "A o maior número ")
elif n2 >= n1 and n2 >= n3:
    print(n2, "B o maior número")
else:
    print(n3, "C o maior número")