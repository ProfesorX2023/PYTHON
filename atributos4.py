class Personaje:
    real = False

    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_poter = Personaje("Humano",True,17)
spiderman = Personaje("humano",False,21)
print(f"Hi Harry_Potter are a magician? {harry_poter.magico}, Age? {harry_poter.edad}, Are you a {harry_poter.especie}?")
print(f"Hi Spyderman are a magician? {spiderman.magico}, Age? {spiderman.edad}, Are you a {spiderman.especie}?")
