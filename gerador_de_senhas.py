import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Pegando a escolha do usuário
while True:
    try:
        tamanho = int(input("Escolha o tamanho da senha (entre 8 e 15 caracteres): "))
        if 8 <= tamanho <= 15:
            break
        else:
            print("❌ O número precisa estar entre 8 e 15!")
    except ValueError:
        print("❌ Por favor, digite um número válido!")

senha = gerar_senha(tamanho)
print(f"🔑 Senha gerada: {senha}")
