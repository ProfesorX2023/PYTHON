#importar bibliotecas
from random import choice

#elegir palabra al azar
def palabra_al_azar():
    palabras=['municipalidad','guatemala','chile','calabaza','sandalias']
    return choice(palabras)

#mostrar guiones
def mostrar_guiones(palabra_secreta):
    guiones=[]
    for n in palabra_secreta:
        guiones.append("_")
    return guiones

#verificar
def verificar():
    letra = "%"
    while letra not in "abcdefghijklmnñopqrstuvwxyz":
        letra = input("Ingrese una letra válida")
    return letra

#comienzo del juego

palabra_secreta=list(palabra_al_azar())
guiones=mostrar_guiones(palabra_secreta)
lista_incorrectas=[]
vidas=6

print("Bienvenidos al juego del ahorcado")
print("Tienes 6 vidas para adivinar la palabra")
print("tu palabra saldrá al final ya sea si aciertas o si pierdes")
print("Ingresa una letra")

while True:
    intento=verificar()
    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento == palabra_secreta[n]:
                guiones[n] =intento
                print(guiones)
        if guiones == palabra_secreta:
            print("Felicidades has ganado")
            palabra="".join(palabra_secreta)
            print(f"la palabra secreta era {palabra}")
            break
    else:
        lista_incorrectas.append(intento)
        print("Lista de incorrectas")
        print(lista_incorrectas)
        vidas -=1
        print(f"te quedan {vidas} vidas")
        if vidas == 0:
            print("GAME OVER")
            palabra="".join(palabra_secreta)
            print(f"la palabra secreta era {palabra}")
            break
