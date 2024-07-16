from flask import Flask, request, jsonify
from data import BD, encontrar_cuenta, Operacion

app = Flask(__name__)

@app.route('/billetera/contactos')
def contactos():
    numero = request.args.get('minumero')
    cuenta = encontrar_cuenta(numero)
    if cuenta:
        contactos_list = [f"{contacto}:{encontrar_cuenta(contacto).nombre}" for contacto in cuenta.contactos]
        return jsonify(contactos_list)
    return "Cuenta no encontrada", 404

@app.route('/billetera/pagar')
def pagar():
    numero = request.args.get('minumero')
    numero_destino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))
    
    cuenta_origen = encontrar_cuenta(numero)
    cuenta_destino = encontrar_cuenta(numero_destino)
    
    if cuenta_origen and cuenta_destino and numero_destino in cuenta_origen.contactos:
        if cuenta_origen.saldo >= valor:
            cuenta_origen.saldo -= valor
            cuenta_destino.saldo += valor
            operacion_origen = Operacion('Pago realizado', valor, numero_destino=numero_destino)
            operacion_destino = Operacion('Pago recibido', valor, numero_origen=numero)
            cuenta_origen.agregar_operacion(operacion_origen)
            cuenta_destino.agregar_operacion(operacion_destino)
            return f"Realizado en {operacion_origen.fecha}"
        return "Saldo insuficiente", 400
    return "Cuenta no encontrada o destinatario no es contacto", 404

@app.route('/billetera/historial')
def historial():
    numero = request.args.get('minumero')
    cuenta = encontrar_cuenta(numero)
    if cuenta:
        historial_list = [f"{op.tipo} de {op.monto} {('a ' + op.numero_destino) if op.numero_destino else ('de ' + op.numero_origen)} en {op.fecha}" for op in cuenta.historial]
        return jsonify({
            "Saldo de " + cuenta.nombre: cuenta.saldo,
            "Operaciones de " + cuenta.nombre: historial_list
        })
    return "Cuenta no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)
