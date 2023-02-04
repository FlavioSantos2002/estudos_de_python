a = int(input('digite um numero: '))
print(f'TABUADDA DO NUMERO {a}')
while a >= 0:
    print('_'*10)
    for c in range(1, 10):
        d = c*a
        print(f'{c} * {a} = {d}')
    print('_'*10)
    a = int(input('digite um numero: '))
else:
    print('fim do programa ate mais tarde')
