class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantano Crias")

class Ormitorrinco(Ave,Reptil,Pez,Mamifero):
    pass

pedro = Ormitorrinco()

pedro.nadar()
print(pedro.tiene_pico)
pedro.caminar()