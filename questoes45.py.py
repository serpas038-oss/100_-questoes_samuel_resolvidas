inicio = int(input("Digite o primeiro Valor: "))
fim = int(input("Digite o último Valor: "))
passo = int(input("Digite o incremento: "))


print("Contagem: '", end="")

if inicio <= fim:
    atual = inicio
    while atual <= fim:
        print(atual, end="' " if atual + passo > fim else " ")
        atual += passo

else:
    atual = inicio
    while atual >= fim:
        print(atual, end="' " if atual - passo < fim else " ")
        atual -= passo

print("Acabou!")