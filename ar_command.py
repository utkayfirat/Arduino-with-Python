from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM
import time


class ArCommand():
    board = Arduino('COM5')
    ledPin = 8
    #it = util.Iterator(board)
    #it.start()

    def openLed(self):
        self.board.digital[self.ledPin].write(1)

    def closeLed(self):
        self.board.digital[self.ledPin].write(0)



