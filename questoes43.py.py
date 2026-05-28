numero = int(input("Digite um valor: "))

if numero > 0:
    print("Contagem: ", end="")
    
        for i in range(1, numero + 1):
        print(i, end=" ")
    
    print("Acabou!")
else:
    print("Por favor, digite um número inteiro e positivo.")