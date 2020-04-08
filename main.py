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

    def __init__(self, placa, pino, delay, funcao):
        self.placa = placa
        self.pino = pino
        self.delay = delay
        self.funcao = funcao

        if self.funcao == 0:
            ligar(self.placa, self.pino, self.delay)
            desligar(self.placa, self.pino, self.delay)
        elif self.funcao == 1:
            ligar(self.placa, self.pino, self.delay)
        elif self.funcao == 2:
            desligar(self.placa, self.pino, self.delay)


placa = Arduino('/dev/ttyACM1')
pinos_btn = [2, 3, 4]
pinos_leds = [5, 6, 7, 8, 9, 10, 11, 12, 13]
tempo = 0.1 # delay

print('Olá Mundo!')

while True:

    for pino in pinos_leds:
        bar_led = BarLed(placa, pino, tempo, 0)
    for pino in pinos_leds:
        bar_led = BarLed(placa, pino, tempo, 1)
    for pino in range(pinos_leds[-1], pinos_leds[0], -1):
        bar_led = BarLed(placa, pino, tempo, 2)
