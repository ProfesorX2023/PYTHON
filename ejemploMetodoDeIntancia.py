class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flechas(self):
        self.cantidad_flechas = self.cantidad_flechas-1

robbin_Hood = Personaje(5)

print(f"Robbin Hood tiene {robbin_Hood.cantidad_flechas} flechas")
robbin_Hood.lanzar_flechas()
print(f"Robbin Hood tiene {robbin_Hood.cantidad_flechas} flechas")
robbin_Hood.lanzar_flechas()
print(f"Robbin Hood tiene {robbin_Hood.cantidad_flechas} flechas")
robbin_Hood.lanzar_flechas()
print(f"Robbin Hood tiene {robbin_Hood.cantidad_flechas} flechas")
robbin_Hood.lanzar_flechas()
print(f"Robbin Hood tiene {robbin_Hood.cantidad_flechas} flechas")
robbin_Hood.lanzar_flechas()
print(f"Robbin Hood tiene {robbin_Hood.cantidad_flechas} flechas")



