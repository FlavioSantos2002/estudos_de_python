letra = input('digite uma letra: ')
a = 0
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'a letra {letra} é vogal')
    a = 1
if letra == 'b' or letra == 'c' or letra == 'd' or letra == 'f' or letra == 'g' or letra == 'h' or letra == 'j' or letra == 'k' or letra == 'l' or letra == 'm' or letra == 'n' or letra == 'p' or letra == 'q' or letra == 'r' or letra == 's' or letra == 't' or letra == 'v' or letra == 'x' or letra == 'w' or letra == 'y' or letra == 'z':
    print('é consoante')
    a = 1
if a == 0:
    print('é um numero')