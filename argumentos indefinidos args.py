def suma_cuadrados(*args):
    total=0
    for arg in args:
        total=arg**2+total

    return nombre, total

print(suma_cuadrados(2,3,4,5,6))

