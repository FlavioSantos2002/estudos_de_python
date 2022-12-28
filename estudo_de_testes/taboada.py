#o usuario da um numero e devemos dar a ataboada completa dele de 1 a 10
a = int(input('digite o numero inteiro: '))
for c in range(1, 11):
    w = c * a
    print('|{:^}*{:^2}={:^2} |'.format(c, a, w))