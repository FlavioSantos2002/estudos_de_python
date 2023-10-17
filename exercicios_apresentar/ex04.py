# Exercício: Separar números pares e ímpares em listas

# Inicializar listas vazias para números pares e ímpares
numeros = []
pares = []
impares = []

# Solicitar ao usuário para inserir números na lista
n = int(input("Quantos números você deseja inserir na lista? "))
for i in range(n):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# Separar números pares e ímpares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Exibir os números pares e ímpares
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
