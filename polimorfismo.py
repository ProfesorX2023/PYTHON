class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "Dice Muuuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + "Dice beee")

vaca1 = Vaca("Lola")
oveja1 = Oveja("Nube")
vaca2 = Vaca("Aurora")
oveja2 = Oveja("Lala")

#con iteraciones
"""animales = [vaca1,oveja1,vaca2,oveja2]

for animal in animales:
    animal.hablar()"""

#con funciones
def animal_hablar(animal):
    animal.hablar()

animal_hablar(oveja1)