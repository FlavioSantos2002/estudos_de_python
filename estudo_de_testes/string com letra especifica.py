#fazer um programa que leia uma string e imprima apenas palavras com letra inicial especificada pelo usuario
frase = 'minha terra tem palmeiras onde canta o sabia e as aves que aqui gogeam não gogeam como la, inclusive atirei o pau no gato e o gato não morreu'
frase = frase.upper()
a = frase.split()
v = 0
letra = str(input('qual letra: '))
letra = letra.upper()
for i in range(0, len(a)):
    if a[v][0] == letra:
        print(a[v])
        v = v + 1
    else:
       v = v + 1



