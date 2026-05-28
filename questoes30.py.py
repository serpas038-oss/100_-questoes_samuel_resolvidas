
l1 = float(input("Digite o 1º lado: "))
l2 = float(input("Digite o 2º lado: "))
l3 = float(input("Digite o 3º lado: "))


if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("\nOs segmentos formam um triângulo!")
    
    
    if l1 == l2 == l3:
        tipo = "EQUILÁTERO"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo = "ISÓSCELES"
    else:
        
        tipo = "ESCALENO'" 
    
    print(f"Classificação: {tipo}")
else:
    print("\nOs segmentos NÃO podem formar um triângulo.")