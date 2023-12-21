class Casa:

    def __init__(self,color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("Blanco",5)
print(f"Mi casa es color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos")