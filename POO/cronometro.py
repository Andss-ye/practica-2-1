from hora import Hora
from minuto import Minuto
from segundo import Segundo
from dia import Dia

class Cronometro():
    def __init__(self):
        self.hora = Hora()
        self.minuto = Minuto()
        self.segundo = Segundo()
        self.dia = Dia()
    def avanzar(self):
        self.segundo.avanzar()
        if self.segundo.valor == 0:
            self.minuto.avanzar()
            if self.minuto.valor == 0:
                self.hora.avanzar()
                if self.hora.valor == 0:
                    self.dia.avanzar()