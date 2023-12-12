palabra='cascaRraBias'
def ordenar(palabra):
    lista=list(palabra.lower())
    conjunto=set(lista)
    resultado=list(conjunto)
    resultado.sort()

    return resultado

print(ordenar(palabra))