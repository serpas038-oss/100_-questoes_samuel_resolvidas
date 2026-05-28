def Contador(inicio, fim, incremento):
    if incremento == 0:
        print('O incremento nao pode ser zero.')
        return
        
    atual = inicio
    
    if incremento > 0:
        while atual <= fim:
            print(atual, end=' ')
            atual += incremento
    
    else:
        while atual >= fim:
            print(atual, end=' ')
            atual += incremento
    print()

v_inicio = int(input('Digite o valor de inicio: '))
v_fim = int(input('Digite o valor de fim: '))
v_incremento = int(input('Digite o incremento: '))

Contador(v_inicio, v_fim, v_incremento)