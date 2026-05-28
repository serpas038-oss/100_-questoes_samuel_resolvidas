def Fibonacci(termos):
    t1 = 1
    t2 = 1
    
    for c in range(termos):
        print(t1, end=' >> ')
        t3 = t1 + t2
        t1 = t2
        t2 = t3
    print('FIM')

qtd = int(input('Digite a quantidade de termos: '))

Fibonacci(qtd)