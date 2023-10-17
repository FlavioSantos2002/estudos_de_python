# Exercício: Calcular a área de um círculo usando uma função

import math

# Definir a função para calcular a área do círculo
def calcular_area_circulo(raio):
    return math.pi * raio ** 2

# Solicitar ao usuário o valor do raio
raio = float(input("Digite o raio do círculo: "))

# Chamar a função e armazenar o resultado em uma variável
area = calcular_area_circulo(raio)

# Exibir o resultado
print(f"A área do círculo com raio {raio} é {area:.2f}.")
