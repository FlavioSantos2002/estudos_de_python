frase = 'minha terra tem palmeiras onde canta o sabia e as aves que aqui gogeam não gogeam como la, inclusive atirei o pau no gato e o gato não morreu'
a = frase.split()
b = []
for v in range(0, len(a)):
    b = b + [a[v][0]]
print(b)