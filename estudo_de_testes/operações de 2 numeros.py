#peça 2 numeros e pergunte qual operação será feita, apois isso imprima informando se o numero é par ou impar, inteiro ou decimal,  positivo ou negativo
n1 = float(input('dê o primeiro numero: '))
n2 = float(input('dê o segundo numero: '))
r = str(input('qual operação deseja fazer (s para soma, m, para multiplicação, d para divisão): '))
r = r.upper()
while True:
    if (r != 'S') and (r != 'M') and (r != 'D'):
        print('OPS! algo deu errado verifique se voce digitou r,s ou d')
        r = str(input('qual operação deseja fazer (s para soma, m, para multiplicação, d para divisão): '))
        r = r.upper()
    else:
        break
s = n1+n2
m = n1*n2
if r == 'S':
    print(f'a soma de {n1} e {n2} é: {s}')
elif r == 'M':
    print(f'o produto de {n1} por {n2} é: {m}')
elif r == 'D':
    if n2 == 0:
        print('o resultado da divisão por 0 é incalculavel')
    else:
        print(f'a quaciente da divisão {n1} por {n2} é: {n1/n2}')