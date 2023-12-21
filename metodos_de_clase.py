class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self,metros):
        print(f"el parajo vuela {metros} metros")
        self.piar()

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

