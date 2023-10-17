seu_dinheiro = int(input('digite quanto você tem: '))
valor_produto = int(input('digite o valor da compra: '))

notas = [100, 50, 20, 10, 5, 2, 1]
soma_das_notas = 0 
resto = 0

if (seu_dinheiro < valor_produto):
    print('saldo insuficiente')
else:
    for c in list(notas):
        soma_das_notas = soma_das_notas + valor_produto//c
        print(f'{valor_produto//c} notas de {c}')
        resto = valor_produto%c
        valor_produto = resto
        if(resto==0):
            break
print('total de notas usadas: ', soma_das_notas)
    
