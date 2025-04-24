notas = [6, 7, 6.5, 4.8, 8]
soma = 0

'''for i in range(5):
    soma = soma + notas[i]'''
    
for i in notas:
       soma += i
    
    
media = soma / 5

print(f'A média final é {round(media, 2)}')