from random import *
def lanzar_dados():
    '''devuelve una tupla con los dados'''
    return randint(1,6), randint(1,6)

def evaluar_jugada(dado1,dado2):
    suma=dado1+dado2
    if suma<=6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif suma>6 and suma<10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    elif suma>=10:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"

a,b=lanzar_dados()
print(evaluar_jugada(a,b))