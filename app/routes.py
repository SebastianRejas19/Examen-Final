
from flask import Blueprint, request, jsonify
from .models import cuentas

bp = Blueprint('main', __name__)

@bp.route('/billetera/contactos')
def listar_contactos():
    numero = request.args.get('minumero')
    cuenta = next((c for c in cuentas if c.numero == numero), None)
    if cuenta:
        contactos = {contacto: next((c.nombre for c in cuentas if c.numero == contacto), "") for contacto in cuenta.contactos}
        return jsonify(contactos)
    return jsonify({"error": "Cuenta no encontrada"}), 404

@bp.route('/billetera/pagar')
def pagar():
    numero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))
    cuenta = next((c for c in cuentas if c.numero == numero), None)
    destino = next((c for c in cuentas if c.numero == numerodestino), None)
    if cuenta and destino:
        if cuenta.transferir(destino, valor):
            return jsonify({"mensaje": f"Transferencia de {valor} realizada con éxito"})
        return jsonify({"error": "Saldo insuficiente"}), 400
    return jsonify({"error": "Cuenta no encontrada"}), 404

@bp.route('/billetera/historial')
def historial():
    numero = request.args.get('minumero')
    cuenta = next((c for c in cuentas if c.numero == numero), None)
    if cuenta:
        return jsonify({
            "saldo": cuenta.saldo,
            "historial": cuenta.historial
        })
    return jsonify({"error": "Cuenta no encontrada"}), 404
