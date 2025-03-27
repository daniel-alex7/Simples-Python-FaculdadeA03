peso = float(input("Digite o valor do peso: "))
altura = float(input("Digite o valor da altura: "))

IMC = peso / altura**2

if IMC < 20:
    print("Abaixo do peso")
    
elif IMC < 25 :
    print("Peso normal")
    
elif IMC < 30 :
    print("Sobrepeso")
    
elif IMC < 40: 
    print("Obeso")
    
else: 
    print("Obeso mórbido")
    
