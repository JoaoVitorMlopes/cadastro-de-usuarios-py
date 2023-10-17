import PySimpleGUI as sg
layout = [

    [sg.Text('usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],

    ]

window = sg.Window('login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'login':
       senha_correta = '123456'
       usuario_correto = 'joao'
       usuario = values['usuario']
       senha = values['senha']

       if senha == senha_correta and usuario == usuario_correto:
           window['mensagem'].update('login feito sucesso')
       else:
           window['mensagem'].update('senha ou usuario incorreto')
