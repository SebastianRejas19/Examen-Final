
from datetime import datetime

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.historial = []

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.recibir(valor, self.numero)
            self.historial.append(f"Pago realizado de {valor} a {destino.nombre} en {datetime.now()}")
            return True
        return False

    def recibir(self, valor, origen):
        self.saldo += valor
        self.historial.append(f"Pago recibido de {valor} de {origen} en {datetime.now()}")

cuentas = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"])
]
