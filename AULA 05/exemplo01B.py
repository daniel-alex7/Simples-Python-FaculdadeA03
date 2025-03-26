m1 = float(input("Digite a media final do aluno: "))
f1 = float(input("Digite a frequência do aluno em %: "))

if f1 < 75:
    
    print("Reprovado por falta")
    print("Sua frequência foi {} e sua nota {}".format(f1, m1))
    print("")
    
elif m1 < 6: 
       
        print("Reprovado por nota sua nota foi: {} e sua frequência {}".format(m1,f1))
        print("")

else:   
        
        print("Aprovado")
        print("Com média {} e frequência {}".format(m1,f1))
        print("")
     