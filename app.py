from flask import Flask, request, render_template
from twilio.rest import Client

app = Flask(__name__)

ACCOUNT_SID = 'ACb7bd7e0d44c8cda936b61706a5569619'
AUTH_TOKEN = '23a70217d94ad61a9d5617ad88c50ddc'
FROM_NUMBER = '+19786439831'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/llamadas")
def llamadas():
    return render_template("llamadas.html")

@app.route("/call", methods=["POST"])
def call():
    numero_destino = request.form.get("numero")
    if not numero_destino:
        return "Falta número", 400

    llamada = client.calls.create(
        to=numero_destino,
        from_=FROM_NUMBER,
        twiml='<Response><Say voice="alice" language="es-ES">Hola, esta es una llamada de prueba de Volpulse. Gracias por contestar.</Say></Response>'
    )
    return f"Llamada iniciada, SID: {llamada.sid}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




