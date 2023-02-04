dados = {"filme": str(input('digite o nome do filme: ')), 'data' : str(input('digite a data: ')), "direção" : str(input('digite o nome do diretor do filme: '))}
a = dados.items
#print(dados.items(),"\n\n")
print(a)

for c in dados.items():
    print(c)
