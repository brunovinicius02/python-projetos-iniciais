import random

def rolar_dados(qtd_dados, lados):
    return [random.randint(1, lados) for _ in range(qtd_dados)]

while True:
    qtd_dados = int(input("Quantos dados deseja rolar? "))
    lados = int(input("Quantos lados cada dado deve ter? (ex: 6 para um D6) "))
    
    resultados = rolar_dados(qtd_dados, lados)
    print(f"\n🎲 Resultado dos dados: {resultados}\n")

    if input("Rolar novamente? (s/n): ").lower() != "s":
        break

print("Obrigado por jogar!")
