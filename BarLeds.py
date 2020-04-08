"""
* BAPDS
* Acionamento de barreira de Leds
* Placa Arduino Mega 2560
"""
from pyfirmata import Arduino, util
import time


# função para ligar uma saída
def ligar(placa, pino, delay):
    placa.digital[pino].write(1)
    print("LED ligado, pino: " + str(pino))
    time.sleep(delay)  # delay(1000);


# função para desligar uma saída
def desligar(placa, pino, delay):
    placa.digital[pino].write(0)
    print("LED desligado, pino: " + str(pino))
    time.sleep(delay)  # delay(1000);


class BarLed():

    def __init__(self, placa, pinos, delay, funcao):
        self.placa = placa
        self.pinos = pinos
        self.delay = delay
        self.funcao = funcao

        if self.funcao == 0:
            for pino in self.pinos:
                ligar(self.placa, pino, self.delay)
                desligar(self.placa, pino, self.delay)
        elif self.funcao == 1:
            for pino in self.pinos:
                ligar(self.placa, pino, self.delay)
            for pino in range(self.pinos[-1], self.pinos[0], -1):
                desligar(self.placa, pino, self.delay)

        elif self.funcao == 2:
            for pino in self.pinos:
                ligar(self.placa, pino, self.delay)
            for pino in range(self.pinos[-1], self.pinos[0], -1):
                desligar(self.placa, pino, self.delay)


placa = Arduino('/dev/ttyACM1')  # declaração da placa e qual a porta de comunicação

it = util.Iterator(placa)                         #
it.start()
time.sleep(1)

pinos_leds = [5, 6, 7, 8, 9, 10, 11, 12, 13]  # pinos de saídas ligados aos Leds, não pode ser maior que 13

tempo = 0.1  # delay

btn1 = placa.get_pin('d:2:i')
btn2 = placa.get_pin('d:3:i')
btn3 = placa.get_pin('d:4:i')

# Principal
while True:
    estado_btn1 = btn1.read()
    estado_btn2 = btn2.read()
    estado_btn3 = btn3.read()

    if estado_btn1:
        funcao = 0
        bar_led = BarLed(placa, pinos_leds, tempo, funcao)
    elif estado_btn2:
        funcao = 1
        bar_led = BarLed(placa, pinos_leds, tempo, funcao)
    elif estado_btn3:
        funcao = 2
        bar_led = BarLed(placa, pinos_leds, tempo, funcao)

    time.sleep(tempo)
