s = 0
v = 0
for c in range(3, 500, 6):
    s = s + c
    if s != 0:
        v = v+1
    print(c)
print(s)
print('sao {} valores'.format(v))
