#fazer uma classe a qual terao funcionalides de uma tv, entre elas estao
#liga desliga, e trocar canais com uma condiçao especial, se vc passar do numero max de canais
#voce vai para o minimo e vice versa

class televisao:
    def __init__(self, canal, minimo, maximo):
        self.canal = canal
        self.maximo = maximo
        self.minimo = minimo
        while True:
            if canal < minimo or canal > maximo:
                canal = int(input('valor invalido digite outro dento dos limites dos canais: '))
            else:
                self.canal = canal
                break
    def CHmais(self):
        if self.canal == self.maximo:
            self.canal = self.minimo
            print(f'o canal é {self.canal}')
        else:
            self.canal += 1
            print(f'o canal é {self.canal}')
    def CHmenos(self):
        if self.canal == self.minimo:
            self.canal = self.maximo
            print(f'o canal é {self.canal}')
        else:
            self.canal -= 1
            print(f'o canal é {self.canal}')
    def trocar_canal(self):
        while True:
            try:
                self.NC = int(input('digite o canal '))
                if self.NC > self.maximo or self.NC < self.minimo:
                    print('passou os limites, tente denovo')
                    continue
                else:
                    self.canal = self.NC
                    print(f'o canal é {self.canal}')
                    break
            except:
                print('certifique-se de digitar apenas numeros')
                continue
    def desliga(self):
        print("tv desliga")

a = 0
x = x2 = x3 =  0
while True:
    try:
        if a == 0:
            x3 = int(input('digite o maximo de canais '))
            x2 = int(input('digite o minimo de canais '))
            x = int(input('digite o numero do canal '))
            tv = televisao(x, x2, x3)
            a = 1
    except:
        print('certifique-se de digitar apenas numeros')
        continue

    controlhe = str(input('digite + para subir o canal ou - para descer, m para trocar manualmente ou s para sair e desligar a tv: '))
    if controlhe == '+':
        tv.CHmais()
    elif controlhe == '-':
        tv.CHmenos()
    elif controlhe == 'm':
        tv.trocar_canal()
    elif controlhe == 's':
        tv.desliga()
        break
    else:
        print('digite apenas o recomendado')
        continue