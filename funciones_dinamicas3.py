def suma_menores(lista_numeros):
    suma=0
    for n in lista_numeros:
        if n in range(0,1000):
            suma=suma+n
        else:
            pass
    return suma
lista_numeros=[1,500,900,1002]
print(suma_menores(lista_numeros))
