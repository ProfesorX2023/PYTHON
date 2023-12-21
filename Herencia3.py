class Mascota:
    def __init__(self,edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

Firulais = Perro(6,"Firulais",4)

print(Firulais.edad)