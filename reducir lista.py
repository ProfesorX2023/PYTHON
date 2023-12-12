lista_numeros=[1,2,15,7,2]
def reducir_lista(lista):
    lista2=list(set(lista))
    lista2.pop()
    return lista2
def promedio(lista):
    suma=sum(lista)
    pro=suma/len(lista)
    return pro



print(reducir_lista(lista_numeros), promedio(reducir_lista(lista_numeros)))
