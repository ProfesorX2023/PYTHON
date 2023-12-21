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

    @staticmethod
    def mirar():
        #self.color = "Rojo" esto no se puede hacer no cambia instancias
        #cls.alas = 2 No puede acceder a los atributos de la clase
        print("el pajaro mira")

    @staticmethod
    def morir():
        print(" El pajaro se murio")



Pajaro.morir()