class Persona:
    nombre = "Luis"
    apeliido = "Xutuc"

    @classmethod
    def ingresoDeDatos(cls, nombre,apellido):
        cls.nombre = nombre
        cls.apellido =apellido

class Cliente(Persona):

    def __init__(self, numeroDeCuenta, balance):
        self.numeroDeCuentra = numeroDeCuenta
        self.balance = balance

    def depositar(self,deposito):
        self.balance = self.balance + deposito

    def retirar(self, retiro):
        self.balance = self.balance - retiro

    def __str__(self):
        return f"Numero de cuenta: {self.numeroDeCuentra}, Balance: {self.balance}"

cliente1 = Cliente("123456789",1000)

"""cliente1.retirar(50)
cliente1.depositar(270)
print(cliente1)"""

def crear_cliente():
    nombre = input("ingresa tu nombre")
    apellido = input("ingresa tu apellido")
    Persona.ingresoDeDatos(nombre, apellido)

def inicio():
    print(f"hola {Persona.nombre} {Persona.apellido}")
    while True:
        print("*" * 15)
        print("*" + "1. Depositar " + "*")
        print("*" + "2. Retirar " + " " * 2 + "*")
        print("*" + "3. Saldo " + " " * 4 + "*")
        print("*" + "4. Salir " + " " * 4 + "*")
        print("*" * 15)
        opcion = input("Ingrese una opcion válida")
        if opcion == "1":
            deposito = int(input("ingrese la cantiadad que desee depositar"))
            cliente1.depositar(deposito)
            print(cliente1)
        elif opcion == "2":
            retiro = int(input("ingrese la cantiadad que desee Retirar"))
            cliente1.retirar(retiro)
            print(cliente1)
        elif opcion == "3":
            print(cliente1)
        elif opcion == "4":
            break
        else:
            print("Ingrese una opción válida")


crear_cliente()

inicio()

