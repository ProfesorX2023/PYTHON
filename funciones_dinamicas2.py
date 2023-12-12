def todos_positivos(lista_numeros):
    lista_positivos=[]
    for n in lista_numeros:
        if n<0:
            return False
        else:
            pass
    return True

print(todos_positivos([1,2,3,-1,-2]))