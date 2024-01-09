def funcion():
    yield "hola"
    yield "hola"
    yield "hola"

variable = funcion()

print(next(variable))
print(next(variable))
print(next(variable))
print(next(variable))