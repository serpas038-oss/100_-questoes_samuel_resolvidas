print("Cálculo de Delta (Δ)")
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))


delta = (b ** 2) - (4 * a * c)

print("-" * 20)
print(f"O valor de Delta é: {delta}")


if delta > 0:
    print("A equação possui duas raízes reais distintas.")
elif delta == 0:
    print("A equação possui uma raiz real (raízes iguais).")
else:
    print("A equação não possui raízes reais.")