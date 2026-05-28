# Solicita o número ao usuário
numero = int(input("Digite um valor: "))

# Verifica se o número é positivo
if numero > 0:
    print("Contagem: '", end="") # Abre a aspas única no início
    
    for i in range(1, numero + 1):
        if i == numero:
            print(i, end="' ") # Fecha a aspas no último número
        else:
            print(i, end=" ")
            
    print("Acabou!")
else:
    print("Por favor, digite um número inteiro e positivo."