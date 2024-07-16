from datetime import datetime

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.historial = []

    def agregar_operacion(self, operacion):
        self.historial.append(operacion)

class Operacion:
    def __init__(self, tipo, monto, numero_destino=None, numero_origen=None):
        self.tipo = tipo
        self.monto = monto
        self.numero_destino = numero_destino
        self.numero_origen = numero_origen
        self.fecha = datetime.now().strftime("%d/%m/%Y")

BD = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"]),
]

def encontrar_cuenta(numero):
    for cuenta in BD:
        if cuenta.numero == numero:
            return cuenta
    return None
