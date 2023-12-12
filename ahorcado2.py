#importar la biblioteca
from random import choice

#elegir palabra al azar

def palabra_azar():
    palabras=['municipalidad','guatemala','sandalias','calabaza','chile']
    return choice(palabras)

#mostrar guiones

def mostrar_guiones(palabra_secreta):
    guiones=[]
    for n in palabra_secreta:
        guiones.append("_")
    return guiones


#verificar si la letra es elegible

def verificar():
    letra= "%"
    while letra not in "abcdefghijklmnñopqrstuvwzyz":
        letra = input("Ingrese una letra")
    return letra

#comienza el juego
palabra_secreta=list(palabra_azar())
guiones=mostrar_guiones(palabra_secreta)
lista_incorrectas=[]
vidas=6

print("Bienvenido al juego del ahorcado")
print("tienes 6 intentos para encontrar la palabra secrea")
print("El juego te dirá en donde aparece cada una de las coincidencias")
print("Al final te mostrará la palabra secreta")
print(guiones)

while True:
    intento = verificar()
    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento == palabra_secreta[n]:
                guiones[n]=intento
                print(guiones)
        if guiones == palabra_secreta:
            print("felicidades has gadado!")
            palabra="".join(palabra_secreta)
            print(f"la palabra era {palabra}")
            break
    else:
        lista_incorrectas.append(intento)
        print("lista de letras incorrectas")
        print(lista_incorrectas)
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
        if vidas == 0:
            print("GAME OVER")
            palabra="".join(palabra_secreta)
            print(f"La palabra secreta era {palabra}")
            break

