#peça 3 numeros inteiros e imprimaos nas seguintes ordens:
# (opção1)crescente, (opção2)decrecente ou (opção3)com o maior no meio
# OBS crie uma estrutura de esolha que pergunte ao usuario qual opção ele vai querer

# ARMAZENANDO AS VARIAVEIS
max = 0
med = 0
min = 0

while True:
    try:
        a, b, c = int(input('digite os numeros: ')), int(input('digite os numeros: ')), int(input('digite os numeros: '))
        break
    except:
        print('digite apenas numeros')
        continue

while True:
    try:
        opcao = int(input('digite o numero da opção: '))
        if opcao == 1 or opcao == 2 or opcao == 3:
            break
    except:
        print('digite apenas numeros')
        continue

#organizando as variavies em ordem crescente

if a >= b and b >= c: #abc
    max = a
    med = b
    min = c
elif a >= c and c >= b:#acb
    max = a
    med = c
    min = b
elif b >= a and a >= c:#bac
    max = b
    med = a
    min = c
elif b >= c and c >= a: #bca
    max = b
    med = c
    min = a
elif c >= a and a >= b: #cab
    max = c
    med = a
    min = b
elif c >= b and b >= a: #cba
    max = c
    med = b
    min = a
if opcao == 2:
    print(max, med, min)
elif opcao == 1:
    print(min, med, max)
else:
    print(min, max, med)