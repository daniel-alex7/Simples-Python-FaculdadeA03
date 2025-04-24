nomes = []
medias = []

x = int(input('Digite a quantidade de alunos: '))

for i in range(x):
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    
    media = (n1 + n2) / 2
    
    nomes.append(nome)
    medias.append(media)
    
n = int(input('Digite o número do aluno que deseja exibir: '))

if medias[n] >= 6.0:
    print(f'O aluno {nomes[n]} foi aprovado com {medias[n]}')
else:
    print(f'O aluno {nomes[n]} foi reprovado com {medias[n]}')