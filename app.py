from flask import Flask, request
import os
from binance.client import Client

app = Flask(__name__)

BINANCE_KEY = os.getenv("BINANCE_KEY")
BINANCE_SECRET = os.getenv("BINANCE_SECRET")

client = Client(BINANCE_KEY, BINANCE_SECRET)

@app.route("/", methods=["GET"])
def index():
    return "Bot rodando!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return "Alerta vazio", 400

    print("Alerta recebido:", data)

    try:
        # Envia uma ordem de compra de $10
        order = client.order_market_buy(
            symbol="BTCUSDT",
            quoteOrderQty=10  # Valor fixo da entrada
        )
        print("Ordem executada:", order)
        return "Ordem enviada!", 200
    except Exception as e:
        print("Erro:", e)
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
