def Potencia(base, expoente):
    return base ** expoente

v_base = float(input('Digite o valor da base: '))
v_expoente = float(input('Digite o valor do expoente: '))

resultado = Potencia(v_base, v_expoente)

print('O resultado da potenciacao e:', resultado)