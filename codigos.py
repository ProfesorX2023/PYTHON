import random
import string

def generar_codigo():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choice(caracteres) for i in range(14))
    return codigo

# Generar 17 códigos
codigos = [generar_codigo() for _ in range(17)]

# Imprimir los códigos generados
for codigo in codigos:
    print(codigo)