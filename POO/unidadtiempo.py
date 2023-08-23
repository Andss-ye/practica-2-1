class UnidadTiempo:
    def __init__(self): #para que todos los metodos esten disponibles en la instanciación
        self.valor = 0
        self.tope = 0

    def avanzar(self):
        self.valor += 1
        if self.valor == self.tope:
            self.valor = 0

if __name__ == "__main__":
    u = UnidadTiempo()
    u.tope = 10
    cont = 0
    while cont < 20:
        print (u.valor)
        u.avanzar()
        cont += 1