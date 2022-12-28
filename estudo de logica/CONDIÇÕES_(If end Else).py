import random
nun = int(random.randint(0, 10))
comp = int(input('PENSEI EM UM NUMERO DE 0 À 10, VC CONSEGUE ADIVINHAR?  '))
print(nun)
i = 0
while nun != comp:
    comp = int(input('tente novamente: '))
else:
    print('vc acertou')

