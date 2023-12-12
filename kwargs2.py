def datos(**kwargs):
    
    for clave,valor in kwargs.items():
        print(f"{clave} : {valor}")





datos(nombre="luis",edad=19,estado="soltero")