class Cubo:
    caras = 6
    def __init__(self, color,forma):
        self.color = color
        self.forma = forma
cubo_rojo = Cubo("rojo","regular")
cubo_verde = Cubo("verde","comprimido")
cubo_azul = Cubo("azul","alargado")

print(f"Cubo de color {cubo_rojo.color} de forma {cubo_rojo.forma}")
print(f"Cubo de color {cubo_verde.color} de forma {cubo_verde.forma}")
print(f"Cubo de color {cubo_azul.color} de forma {cubo_azul.forma}")
