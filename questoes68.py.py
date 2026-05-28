total_mulheres = 0
soma_peso_mulheres = 0
homens_mais_100 = 0
maior_peso_homem = 0

print("--- CADASTRO DE PESO E GÊNERO ---")

for i in range(1, 9):
    print(f"--- {i}ª PESSOA ---")
    sexo = input("Sexo [M/F]: ").strip().upper()
    peso = float(input("Peso (Kg): "))

   
    if sexo == 'F':
        total_mulheres += 1
        soma_peso_mulheres += peso
    
    
    elif sexo == 'M':
        if peso > 100:
            homens_mais_100 += 1
        
        
        if peso > maior_peso_homem:
            maior_peso_homem = peso