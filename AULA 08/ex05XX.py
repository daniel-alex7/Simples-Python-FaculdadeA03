texto = input("Digite um texto: ")

pontua = [".",",",":",";","!","?"] 

#remover sinais de pontuação

for p in pontua:
    texto = texto.replace(p, " ")

#split para devolver lista com as palavras como itens

lista = texto.split()
numero = len(lista)

print(f"O número de palavras é: {numero}")
   



