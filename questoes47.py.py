soma = 0
inicio = 6
fim = 100
incremento = 2

print("Sequência: '", end="")

# O range vai de 6 até 100 (usamos 101 pois o limite superior é exclusivo)
for i in range(inicio, fim + 1, incremento):
    soma += i
    
    # Lógica para fechar a aspas no último número
    if i >= fim:
        print(i, end="'")
    else:
        print(i, end=" + ")

print(f"\nO resultado da soma é: {soma}")