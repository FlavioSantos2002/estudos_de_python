import random
a = (random.randint(0, 100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))
print(a, 'primeira ordem')
b = sorted(a)
print(b, 'organizado')
print(f'o menor é {b[0]}, posçao{a.index(b[0])}' f' ja o maior é {b[4]}, posçao{a.index(b[4])}')




