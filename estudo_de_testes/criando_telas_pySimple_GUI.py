from PySimpleGUI import PySimpleGUI as sg
#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key = 'Usuario', size = (20, 1))],
    [sg.Text('Senha'), sg.Input(key = 'Senha', password_char='*', size = (20, 1))],
    [sg.Checkbox('salvar o login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de login', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuario'] == 'Flavio' and valores['Senha'] == '123456':
            print('bem vindo Flavio')
        else:
            print(' senha ou usuario errados')