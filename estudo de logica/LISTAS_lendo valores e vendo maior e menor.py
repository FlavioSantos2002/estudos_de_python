a = list(range(0, 5))
print(a)
for c in range(0, 5):
    b = int(input('digite um numero; '))
    a[c] = b
print(a, end=' ')
w = sorted(a)
print(f'o maior é {w[4]}, ja o menor é {w[0]}')
