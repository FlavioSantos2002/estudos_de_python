# Exercício: Jogo de adivinhação

import random

# Gerar um número aleatório entre 1 e 100
numero_correto = random.randint(1, 10)

# Inicializar a variável de tentativas
tentativas = 0

# Iniciar o loop while
while True:
    # Solicitar ao usuário para adivinhar o número
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    
    # Incrementar o número de tentativas
    tentativas += 1
    
    # Comparar o palpite com o número correto
    if palpite == numero_correto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s)!")
        break
    elif palpite < numero_correto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

