class Pajaro:
    alas = True

    def __init__(self, color,especie):
        self.color = color #Por convención lleva 3 veces el nombre
        self.especie = especie

mi_pajaro = Pajaro("Negro",'Tucan')
canario = Pajaro('Amarillo','Canario')

print(f"mi pajaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")
print(f"mi pajaro es un {canario.especie} de color {canario.color}")

