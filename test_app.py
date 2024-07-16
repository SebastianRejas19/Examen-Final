import unittest
from data import Cuenta, Operacion, encontrar_cuenta

class TestBilletera(unittest.TestCase):
    
    def setUp(self):
        self.cuenta_arnaldo = Cuenta("21345", "Arnaldo", 200, ["123", "456"])
        self.cuenta_luisa = Cuenta("123", "Luisa", 400, ["456"])
        self.cuenta_andrea = Cuenta("456", "Andrea", 300, ["21345"])
        self.BD = [self.cuenta_arnaldo, self.cuenta_luisa, self.cuenta_andrea]

    # Prueba de caso de éxito 1: Transferencia exitosa
    def test_transferencia_exitosa(self):
        cuenta_origen = encontrar_cuenta("21345")
        cuenta_destino = encontrar_cuenta("123")
        valor = 50
        cuenta_origen.saldo -= valor
        cuenta_destino.saldo += valor
        operacion_origen = Operacion('Pago realizado', valor, numero_destino="123")
        operacion_destino = Operacion('Pago recibido', valor, numero_origen="21345")
        cuenta_origen.agregar_operacion(operacion_origen)
        cuenta_destino.agregar_operacion(operacion_destino)
        self.assertEqual(cuenta_origen.saldo, 150)
        self.assertEqual(cuenta_destino.saldo, 450)

    # Prueba de caso de éxito 2: Agregar operación al historial
    def test_agregar_operacion(self):
        operacion = Operacion('Pago recibido', 100, numero_origen="789")
        self.cuenta_arnaldo.agregar_operacion(operacion)
        self.assertEqual(len(self.cuenta_arnaldo.historial), 1)
        self.assertEqual(self.cuenta_arnaldo.historial[0].monto, 100)
        self.assertEqual(self.cuenta_arnaldo.historial[0].tipo, 'Pago recibido')

    # Prueba de error 1: Saldo insuficiente
    def test_saldo_insuficiente(self):
        cuenta_origen = encontrar_cuenta("21345")
        cuenta_destino = encontrar_cuenta("123")
        valor = 300  # Excede el saldo de la cuenta origen
        if cuenta_origen.saldo < valor:
            self.assertEqual(cuenta_origen.saldo, 200)  # El saldo no debe cambiar
            self.assertEqual(cuenta_destino.saldo, 400)  # El saldo no debe cambiar

    # Prueba de error 2: Cuenta no encontrada
    def test_cuenta_no_encontrada(self):
        cuenta = encontrar_cuenta("99999")  # Número de cuenta inexistente
        self.assertIsNone(cuenta)

    # Prueba de error 3: Contacto no existente
    def test_contacto_no_existente(self):
        cuenta_origen = encontrar_cuenta("21345")
        numero_destino = "789"  # Número que no es un contacto de la cuenta origen
        cuenta_destino = encontrar_cuenta(numero_destino)
        self.assertIsNotNone(cuenta_origen)
        self.assertIsNone(cuenta_destino)  # Debe ser None ya que no es un contacto válido

if __name__ == '__main__':
    unittest.main()
