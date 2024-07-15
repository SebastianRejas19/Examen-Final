# Examen-Final

## Caso de Estudio
 Desarrollar un software que implemente una billetera electrónica para Celular, al estilo de Yape
 o Plin.
 Se debe soportar las operaciones:
 
Contactos: Lista los contactos de un número de teléfono con sus nombres.
 Pagar: Transfiere un valor a otro número (debe ser un contacto). La cuenta debe
 tener saldo suficiente para hacer la transferencia.
 Historial: Muestra el saldo y la lista de operaciones, tanto de envío como de recepción
 de dinero.
 
### Pregunta 1
En un repositorio Github, desarrollar el código fuente (se recomienda usar Python, pero no es obligatorio) que implemente los endpoints:

```
/billetera/contactos?minumero=XXXX
/billetera/pagar?minumero=XXXX&numerodestino=YYYY&valor=ZZZZ
/billetera/historial?minumero=XXXX

```

***Comprobamos que el code funciona***
- Contactos:
  <p align="center">
  <img src="contactos.png" alt="Contactos">
</p>

