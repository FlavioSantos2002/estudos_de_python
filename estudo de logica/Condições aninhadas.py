val = int(input('valor da casa: '))
sal = int(input('seu salário: '))
anos = int(input('em quantos anos pretende pagar a casa: '))
VP = int((val/(anos*12)))
if VP > 0.3*sal:
    print('Não podemos financiar essa casa')
else:
    print('bela compra')
