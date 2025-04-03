import math

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c  # Calcula o delta

    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        x = -b / (2*a)
        return f"A equação possui uma única raiz real: x = {x:.2f}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"As raízes da equação são: x1 = {x1:.2f}, x2 = {x2:.2f}"

# Entrada de dados do usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Exibe o resultado
print(calcular_raizes(a, b, c))
