class Padre():
    def trabajar(self):
        print("Trtabajano en el hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalia")

class Hija(Madre,Padre):
    pass

Valentina = Hija()

Valentina.trabajar()
Valentina.reir()
