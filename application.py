from flask import Flask, jsonify
from opengateway_sandbox_sdk import Simswap

application = Flask(__name__)

phone_number = "+34634512787"
simswap_client = Simswap("013ff25c-edc0-462f-bf6a-7880b8937529", "822bb1a7-c036-4add-9315-e441cbd14da5", phone_number)

# Ruta de prueba usando el método 'check'
@application.route('/test_simswap', methods=['GET'])
def test_simswap():
    try:
        # Realizamos la llamada al método 'check' del cliente Simswap
        response = simswap_client.check(11)  # Llamada a la función check()
        
        # Devolver el resultado en formato JSON
        return jsonify({"status": "success", "data": response}), 200
    except Exception as e:
        # Si ocurre algún error, devolverlo como un mensaje JSON
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    application.run(debug=True)

