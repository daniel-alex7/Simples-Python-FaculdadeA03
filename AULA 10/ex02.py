def Calcularimc(altura, peso):
    
  imc = peso / (altura**2)
  return(imc)

def ClassificarImc(argIMC):
    
    if argIMC < 18.5:
        print("Abaixo do peso ideal")
    elif argIMC < 25:
        print("Peso Ideal")
    else:
        print("Acima do Peso")
    return(argIMC)

a = float(input("Digite sua altura: "))
p = float(input("Digite seu peso: "))

ret = Calcularimc(a,p)

c = ClassificarImc(ret) #só chamar variavel dentro do método

print(f"Seu índice de massa é {ret}")
