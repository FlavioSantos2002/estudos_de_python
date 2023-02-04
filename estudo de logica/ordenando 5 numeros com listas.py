k = 0
a = list(range(0, 5))
for c in range(0, 5):
    b = int(input('digite o numero: '))
    a[4-c] = b
print(a)
for x in range(0, 5):
    for y in range(0, 5):
        if a[x] < a[y]:
            k = a[y]
            a[y] = a[x]
            a[x] = k
print(a)