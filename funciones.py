'''

Declara una función llamada saludar, que cada vez que sea llamada imprima
en pantalla "¡Hola mundo!"
Solo debes definir la función, no debes invocarla luego.

'''

lista_numeros=[1,2,-3,4,0]

def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n>=0:
            return True
        else:
            return False

print(todos_positivos(lista_numeros))