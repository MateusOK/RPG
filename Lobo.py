from Monstro import Monstro

class Lobo(Monstro):
    def __init__(self, vida, ataque, tipo, forca):
        super().__init__(vida, ataque, tipo)
        self.forca: int = forca