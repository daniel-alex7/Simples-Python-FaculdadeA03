import math
sombra = float(input("Digite o comprimento da sombra em m:  "))
angulo = float(input("Digite o ângulo em graus:  "))

altura = math.tan(angulo) * sombra
 
print(f"A altura do prédio é de: {altura}")

