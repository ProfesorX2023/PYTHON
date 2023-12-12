from random import choice

#Esta parte elige una palabra al azar
def palabra_al_azar():
    palabras = ['chile', 'calabaza', 'vestido', 'sandalias', 'responsabilidad','municipalidad','guatemala']
    return choice(palabras)

#esta parte convierte la palabra a guiones
def convertir_guiones(palabra_secreta):
    guiones=[]
    for n in palabra_secreta:
        guiones.append("_")
    return guiones

#Esta parte únicamente verifica si estas poniendo una letra
def verificar():
    letra="%"
    while letra not in "abcdefghijklmnopqrstuvwxyzñ":
        letra = input("ingrese una letra")
    return letra


palabra_secreta=list(palabra_al_azar())
guiones=convertir_guiones(palabra_secreta)
lista_incorrectas=[]
vidas=7
print("Bienvenid@ al juego del ahorcado")
print("El juego trata de qué adivines las palabras")
print("puedes escribir una letra para darte una pista")
print("El juego te díra en donde aparece la letra para reducir la palabra")
print("tienes 7 vidas")
print(guiones)

while True:
    intento=verificar()
    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento==palabra_secreta[n]:
                guiones[n]=intento
                print(guiones)
        if guiones == palabra_secreta:
            print("Felicitaciones has ganado")
            palabra="".join(palabra_secreta)
            print(f"la palabra es {palabra}")
            break
    else:
        lista_incorrectas.append(intento)
        print("Lista de intentos incorrectos")
        print(lista_incorrectas)
        vidas -=1
        print(f"te quedan {vidas} vidas")
        if vidas==0:
            print("Game Over")
            palabra = "".join(palabra_secreta)
            print(f"la palabra era {palabra}")
            break


