CDiaria = str(input("Digite o tipo de diária: S para Simples | D para Duplo | T para Triplo: "))
Qdiaria = int(input("Digite quantos dias ficará hospedado: "))

if CDiaria == 'S' or CDiaria == 's':
    print(f"Em sua diária simples o valor total a pagar será: R${Qdiaria * 255.50}")

elif CDiaria == 'D' or CDiaria =='d':
    print(f"Em sua diária dupla o valor total a pagar será: R${Qdiaria * 305.50}")

elif CDiaria == 'T' or CDiaria =='t':
    print(f"Em sua diária tripla o valor total a pagar será: R${Qdiaria * 360.50}")

else:
    print("Tipo de diária inválida")
    