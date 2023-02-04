#aula sobre dicionario
###se pode declarar um dicionario de 2 formas, em uma delas voce usa 
# o comando dict() e passa os elementos dentro, ou voce 
# os coloca dentro das chaves {}###

dados = {'nome': 'pedro', 'idade': '25'}
#note que pra printar agora nao damos a posição e sim informamos o tipo de dado do dicionario que queremos
#print(dados['idade']) note que informamos o campo idade e ao printar sai 25


#para adicionar elementos basta criar o novo elementop e atribui-lo ao dicionario veja no exemplo

dados['sexo'] = 'masculino'
print(dados)

#e para eliminar elementos bata dar um del

#del dados['idade']
#print(dados)

#\3 metodos importantes:
#--> Nome_do_Dicionario.values() retorna os valores DENTRO do dicionario.
#--> Nome_do_Dicionario.keys() retorna o tipo de dado do dicionario "chaves"
#--> Nome_do_Dicionario.itens() retorna os 2 tipos de dados\#

#print(dados.values())
#print(dados.keys())
print(dados.items())
cont = 0
for v, k in dados.items():
    print(f'o {v} é {k}')
    cont += 1

print(cont)

