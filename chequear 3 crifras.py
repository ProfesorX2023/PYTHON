def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass

    return False



print(chequear_3_cifras([22,99,100,90]))