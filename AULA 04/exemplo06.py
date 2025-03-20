nome = input("Digite o nome do aluno: ")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 6:
    print (f"{nome} foi aprovado(a) sua média({media}) foi maior que 6.0!")
else:
    print(f"Aluno(a) {nome} foi reprovado(a) sua média({media}) foi menor que 6.0")