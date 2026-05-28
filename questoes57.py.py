total_salario_homens = 0
total_salario_mulheres = 0

print("--- CADASTRO DE SALÁRIOS ---")

while True:
    salario = float(input("Salário do funcionário: R$ "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    
    if sexo == 'M':
        total_salario_homens += salario
    elif sexo == 'F':
        total_salario_mulheres += salario
    else:
        print("Sexo inválido! Os dados não foram somados corretamente para este registro.")

    
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    print("-" * 30)
    
    if continuar == 'N':
        break

print(f"Total pago aos homens: R$ '{total_salario_homens:.2f}'")
print(f"Total pago às mulheres: R$ '{total_salario_mulheres:.2f}'"