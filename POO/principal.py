from cronometro import Cronometro

c = Cronometro()

for i in range (100000):
    print (c.dia.valor, c.hora.valor, c.minuto.valor, c.segundo.valor)
    c.avanzar()