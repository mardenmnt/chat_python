from PySimpleGUI import PySimpleGUI as sg
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    print('msg: ' + msg)

TOPICO = 'chat/marden'  # my client
TOPICO_SEND = 'chat/WordSuport' # another client
IP_BROKER = 'test.mosquitto.org'
client = mqtt.Client("marden")  # create new instance
client.on_message = on_message  # attach function to callback
client.connect(IP_BROKER)  # connect to
client.subscribe(TOPICO)

client.loop_start()

sg.theme('GreenTan')  # GreenTan
layout = [
    [sg.Text('Meu nome de Usuario:', size=(18, 1)), sg.Text(TOPICO, size=(12, 1), text_color='red')],
    [sg.Output(size=(50, 20))],
    [sg.Input('Meu primeiro Texto', key='input_msg', size=(45, 7))],
    [sg.Button('Enviar', size=(22, 2)), sg.Button('Exit', size=(22, 2))]
]

janela = sg.Window('Minha primeira Interface', layout)

while True:
    evento, values = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Exit':
        break
    if evento == 'Enviar':
        print('Você: ', values['input_msg'])
        client.publish(TOPICO_SEND, values['input_msg'])
        janela['input_msg'].update('')
janela.close()
client.loop_stop()
