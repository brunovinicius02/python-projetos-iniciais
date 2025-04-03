def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Dicionário com as opções de conversão
conversoes = {
    "C": {"F": celsius_para_fahrenheit, "K": celsius_para_kelvin},
    "F": {"C": fahrenheit_para_celsius, "K": fahrenheit_para_kelvin},
    "K": {"C": kelvin_para_celsius, "F": kelvin_para_fahrenheit},
}

# Interface com o usuário
print("🌡️ Conversor de Temperatura 🌡️")
print("Opções disponíveis: ")
print("C → Celsius")
print("F → Fahrenheit")
print("K → Kelvin")

while True:
    origem = input("\nDigite a unidade de origem (C/F/K): ").strip().upper()
    if origem in conversoes:
        break
    print("❌ Unidade inválida! Escolha entre C, F ou K.")

while True:
    destino = input("Digite a unidade de destino (C/F/K): ").strip().upper()
    if destino in conversoes[origem]:
        break
    print("❌ Conversão inválida! Escolha entre as unidades disponíveis.")

while True:
    try:
        valor = float(input(f"\nDigite a temperatura em {origem}: "))
        break
    except ValueError:
        print("❌ Entrada inválida! Digite um número válido.")

# Fazendo a conversão
resultado = conversoes[origem][destino](valor)

print(f"\n✅ {valor}°{origem} equivale a {resultado:.2f}°{destino}")
