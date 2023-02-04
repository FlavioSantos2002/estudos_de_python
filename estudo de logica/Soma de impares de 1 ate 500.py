s = 0
a = 500//3
if a % 2 != 0:
    Tm = ((a//2)*3)+3
else:
    Tm = 0
for c in range(0, a//2, 3):
    if c/2!=0:
        print(c)
        s = s + (c + (498-(c-3)))
print(s+Tm)
print(Tm)
