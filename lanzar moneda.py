from random import choice
lista_numeros=[1,2,3,4,5,6]
def lanzar_moneda():
    moneda=['Cara','Cruz']
    return choice(moneda)
def probar_suerte(moneda,lista):
    if moneda == 'Cara':
        lista=[]
        return lista
    elif moneda == 'Cruz':
        return lista

print(probar_suerte(lanzar_moneda(),lista_numeros))