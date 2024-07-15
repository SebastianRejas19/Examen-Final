
import unittest
from app.models import Cuenta

class TestCuenta(unittest.TestCase):

    def setUp(self):
        self.cuenta1 = Cuenta("123", "Luisa", 400, ["456"])
        self.cuenta2 = Cuenta("456", "Andrea", 300, ["123"])

    def test_transferencia_exitosa(self):
        resultado = self.cuenta1.transferir(self.cuenta2, 100)
        self.assertTrue(resultado)
        self.assertEqual(self.cuenta1.saldo, 300)
        self.assertEqual(self.cuenta2.saldo, 400)

    def test_transferencia_saldo_insuficiente(self):
        resultado = self.cuenta1.transferir(self.cuenta2, 500)
        self.assertFalse(resultado)
        self.assertEqual(self.cuenta1.saldo, 400)
        self.assertEqual(self.cuenta2.saldo, 300)

    def test_historial_pago_realizado(self):
        self.cuenta1.transferir(self.cuenta2, 100)
        self.assertIn("Pago realizado de 100 a Andrea", self.cuenta1.historial[0])

    def test_historial_pago_recibido(self):
        self.cuenta1.transferir(self.cuenta2, 100)
        self.assertIn("Pago recibido de 100 de 123", self.cuenta2.historial[0])

    def test_contactos(self):
        self.assertIn("456", self.cuenta1.contactos)
        self.assertIn("123", self.cuenta2.contactos)

if __name__ == "__main__":
    unittest.main()
