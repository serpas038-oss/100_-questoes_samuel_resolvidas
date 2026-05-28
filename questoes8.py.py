# Entrada de dados
metros = float(input('Digite uma distância em metros: '))

# Cálculos de conversão
km  = metros / 1000
hm  = metros / 100
dam = metros / 10
dm  = metros * 10
cm  = metros * 100
mm  = metros * 1000

# Saída de dados
print(f"A distância de {metros}m corresponde a:")
print(f'{km:<10} Km')
print(f'{hm:<10} Hm')
print(f'{dam:<10} Dam')
print(f'{dm:<10} dm')
print(f'{cm:<10} cm')
print(f'{mm:<10} mm')
