a = int(input('informe o tamanho dos lados do triangulo: '))
b = int(input('informe o tamanho dos lados do triangulo: '))
c = int(input('informe o tamanho dos lados do triangulo: '))
y = 0
if a+b > c and a+c > b and b+c > a:
    d = 'é um triangulo'
    print(d)
else:
    w = 'Nao é triangulo'
    print(w)
    y = 1
if (a == b and b == c) and (y != 1):
    x = 'equilatero'
    print(x)
elif ((a == b and a != c) or (a == c and a != b) or (b == c and c != a)) and (y != 1):
    t = 'isoceles'
    print(t)
elif (a != b and a != c and b != c) and (y != 1):
    print('escaleno')
