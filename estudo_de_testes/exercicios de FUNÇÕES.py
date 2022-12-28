#varios exercicios so de função, a ideia é chamar a função e exercutar uma tarefa
from math import pi as pi
# 01) criar uma função que dado um raio, calcula o volume e area de uma esfera

def v_a(r):
    V = ((4 * pi) * r ** 3) / 3
    A = 4 * pi * r**2
    print('o volume é {:.2f} e a area é {:.2f}'.format(V, A))
#v_a(int(input('o valor é ')))

# 2)determinar se um numero esta no intervalo determinado pelo usuario

def intervalo(n1, n2, n):
    if (n1 > n and n2 < n) or (n1 < n and n2 > n):
        print('esta no intervalo')
    else:
        print('nao esta no intervalo')
#intervalo(int(input('o valor 1 é ')), int(input('o valor 2 é ')), int(input('o numero é ')))

# 3) função que conta quantas maiusculas e miinusculas em uma str.

def Mai_Min(a):
    b = 0
    maiuscula = 0
    minuscula = 0

    while b != len(a):
        if a[b] == ' ':
            b = b + 1
            continue
        if a[b] == a[b].upper():
            maiuscula = maiuscula + 1
            b = b + 1
        else:
            minuscula = minuscula + 1
            b = b + 1
    print(f'quentidade\nmaiusculas = {maiuscula}\nminusculas = {minuscula}')
#Mai_Min(str(input('digite algo: ')))