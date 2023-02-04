#FAZER UMA LISTA DE FILMES 
#com os elementos nome, ano e diretor

lista_de_filmes = []
cont = 0
valor = int(input("digite o numero de filmes pra lista: "))
while cont<valor:
    nome = str(input('digite o nome do filme: '))
    ano = str(input('digite o ano do filme: '))
    diretor = str(input('digite o nome do diretor do filme: '))

    dic = {"nome" : nome, "ano" : ano, "diretor" : diretor}

    lista_de_filmes = lista_de_filmes + [dic]
    cont += 1
    print(f"\nFilme {cont} listado \n")

cont = 1
print("__________LISTA DE FILMES__________\t")
for c in list(lista_de_filmes):
    print(f"          filme {cont}")
    print(f"nome do filme: {c['nome']}\nano do filme: {c['ano']}\ndiretor: {c['diretor']}\n")
    print("__________________________________\t")
    cont += 1 
    

    





