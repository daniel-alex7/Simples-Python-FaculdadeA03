import math
n1 = float(input("Digite um número real: "))

absoluto = math.fabs(n1)
inteiro = math.trunc(n1)
raiz = math.sqrt(n1)
fatorial = math.factorial(inteiro)

print(f"Abosluto : {absoluto}")
print(f"Inteiro : {inteiro}")
print(f"Raiz : {raiz}")
print(f"Fatorial : {fatorial}")
