def numero_personas(nombre,*args):
    return f"{nombre}, la suma de tus números es {sum(args)}"

print(numero_personas("juan",1,2,3))