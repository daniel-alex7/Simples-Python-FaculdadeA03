num = []
soma = 0

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 0:
        break
    num.append(n)
    
    soma += n
    
media = soma / len(num)

print(f'Lista: {num}')
print(f'Média é {round(media,2)}')