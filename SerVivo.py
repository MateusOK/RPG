class SerVivo:
    def __init__(self, vida, ataque):
        self.ponto_vida: int = vida
        self.ponto_ataque: int = ataque

    def ver_vida(self):
        print("Sua vida atual: ", self.ponto_vida)

    def atacar(self, inimigo):
        if inimigo.ponto_vida > 0:
            inimigo.ponto_vida -= self.ponto_ataque
            print("Inimigo foi atacado!")
            print("Dano causado: ", self.ponto_ataque)
            print("Vida atual do inimgo: ", inimigo.ponto_vida)
        else:
            print("Você não pode atacar este inimgo!")

