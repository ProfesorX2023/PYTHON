class Maestro:
    nombre = "Federico"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno:
    pass

alumno5 = Maestro("Federico",5)

print(alumno5.nombre)