def SuperSomador(n1, n2):
    soma = 0
    
    inicio_intervalo = min(n1, n2)
    fim_intervalo = max(n1, n2)
    
    for c in range(inicio_intervalo, fim_intervalo + 1):
        soma += c
        
    return soma

valor1 = int(input('Digite o valor inicial: '))
valor2 = int(input('Digite o valor final: '))

resultado = SuperSomador(valor1, valor2)

print('A soma do intervalo e:', resultado)