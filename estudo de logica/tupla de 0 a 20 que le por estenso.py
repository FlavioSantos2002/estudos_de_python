a = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorse', 'quinze', 'desesseis', 'desessete', 'dezoito', 'desenove', 'vinte')
b = int(input('digite um numero de 0 a 20: '))
if (20 < b) or (b < 0):
    while (20 < b) or (b < 0):
        print('ops tente novamente')
        b = int(input('digite um numero de 0 a 20: '))
print(f'o numero digitado foi o {a[b]}')
