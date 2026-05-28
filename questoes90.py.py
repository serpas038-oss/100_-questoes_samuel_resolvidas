def Somador(valor1, valor2):
    resultado = valor1 + valor2
    
    print(f"'A soma entre {valor1} e {valor2} é igual a {resultado}'")


num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

print("-" * 40)

Somador(num1, num2)