a = [input('digite algo: ')]
d = []
e = []
for c in list(a[0]):
    if c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == '0':
        d.append(c)
    else:
        e.append(c)
print(d)
print(e)