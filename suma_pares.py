def cantidd_pares(lista_numeros):
    contador=0
    for n in lista_numeros:
        if n%2==0:
            contador = contador+1
        else:
            pass
    return contador

lista_numeros=[2,4,6,7,9,10]
print(cantidd_pares(lista_numeros))