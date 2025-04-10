resp = 's'
soma = 0.0
qntd = 0.0

while resp == 's' or resp == 'S':
    num = float(input("Digite o numero: "))
    soma = soma + num
    qntd = qntd + 1
    resp = input('Deseja continuar? (S/N) ')


media = soma / qntd
print(f'A media entre os números digitados é: {media}')