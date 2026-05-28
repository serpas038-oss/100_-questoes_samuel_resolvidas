inicio = int(input("Digite o primeiro Valor: "))
fim = int(input("Digite o último Valor: "))
incremento = int(input("Digite o incremento: "))

print("Contagem: '", end="")

valores = list(range(inicio, fim + 1, incremento))

for i, num in enumerate(valores):
    if i == len(valores) - 1:
        print(num, end="' ") 
    else:
        print(num, end=" ")

print("Acabou!")