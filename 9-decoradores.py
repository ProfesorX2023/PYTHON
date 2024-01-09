def cambiar_letras(tipo):
    def mayusculas(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas

operacion = cambiar_letras("min")

operacion("Palabra")