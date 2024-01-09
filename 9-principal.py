import numeros

def preguntar():
    print("Bienvenidos a Farmacia Fibonacci")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmética")
        try:
            mi_rubro = input("Elija su rubro").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Quiéres sacar otro turno [S] o [N]").upper()
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita a farmacia Fibonacci")
                break
inicio()
