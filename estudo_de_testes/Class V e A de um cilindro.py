from math import pi


class cilindro:
    def __init__(self, a, r):
        self.r = r
        self.a = a

    def area_cilindro(self):
        self.area = (pi * self.r ** 2) + (self.a * 2 * pi * self.r)
        print('{:.2f}'.format(self.area))

    def volume_cilindro(self):
        self.volume = (pi * self.r ** 2) * self.a
        print('{:.2f}'.format(self.volume))

while True:
    try:
        abacate = cilindro(int(input('valor da altura: ')), int(input('valor do raio: ')))
        break
    except:
        print("\ntente novamente\n")
        continue


while True:
    try:
        x = int(input('\nDigite 1 para area\nDigite 2 para volume '))
        match x:
            case 1:
                abacate.area_cilindro()
                break
            case 2:
                abacate.volume_cilindro()
                break
            case x:
                print("\ntente novamente")

    except:
        print("\ntente novamente")
        continue
