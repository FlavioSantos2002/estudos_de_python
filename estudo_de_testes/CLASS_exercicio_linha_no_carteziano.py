# 1) preencher os metodos de uma class para aceitar coordenadas como um par de tuplas
# e retornar a inclinação e a distancia dos pontos

class coordenadas :
    def __init__(self):
        self.p1 = ((int(input('x1: '))), (int(input('y1: '))))
        self.p2 = ((int(input('x2: '))), (int(input('y2: '))))
    def D_p1_p2(self):
        self.d = (((self.p1[0]-self.p2[0])**2)+(self.p1[1]-self.p2[1])**2)**(1/2)
        print(f'a distancia entres os pontos {self.p1} e {self.p2} é {self.d}')
    def inclinação(self):
        self.i = -((self.p1[1])-self.p2[1])/((self.p2[0])-(self.p1[0]))
        print(f'a inclinação é tangente de({self.i})')
v = coordenadas()
v.D_p1_p2()
v.inclinação()

