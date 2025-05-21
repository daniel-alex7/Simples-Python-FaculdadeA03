#Quando sei que devo ter retorno? Se o resultado precisar usar em outro lugar

def somandoNumeros(numA, numB):
    resu = numA + numB
    return(resu)
    
a = int(input("Digite valor: "))
b = int(input("Digite valor: "))
c = somandoNumeros(a,b)

print(f"Soma de dois números: {c}")
