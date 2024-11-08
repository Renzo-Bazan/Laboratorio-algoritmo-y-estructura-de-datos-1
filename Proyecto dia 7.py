class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_cliente(self):
        print(f"""Nombre: {self.nombre} 
Apellido: {self.apellido} 
Número de cuenta: {self.numero_cuenta} 
Balance: {self.balance}""")

    def depositar(self):
        deposito = float(input("¿Cuánto dinero quiere depositar?: "))
        self.balance = self.balance + deposito

    def retirar(self):
        sacar = float(input("¿Cuánto dinero quiere sacar de la cuenta?: "))
        if sacar <= self.balance:
            self.balance = self.balance - sacar
        else:
            print("No tiene suficiente balance para retirar esa cantidad.")

def crear_cliente():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    balance = float(input("Ingrese el balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)

def inicio():
    cliente = crear_cliente()
    while True:
        cliente.imprimir_cliente()
        accion = input("Que operacion quiere realizar? (depositar/retirar/salir): ").lower()
        if accion == "depositar":
            cliente.depositar()
        elif accion == "retirar":
            cliente.retirar()
        elif accion == "salir":
            break
        else:
            print("Acción no válida. Intente nuevamente.")

inicio()
