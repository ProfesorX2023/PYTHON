def suma_absolutos(*args):
    total=0
    for arg in args:
        total=(arg*arg)**0.5+total
    return total

print(suma_absolutos(-1,-2,3))