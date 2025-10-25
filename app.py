from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from logic import responder

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    mensaje_entrante = request.form.get("Body")
    respuesta = responder(mensaje_entrante)

    twilio_response = MessagingResponse()
    twilio_response.message(respuesta)

    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=True)
