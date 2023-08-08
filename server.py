from flask import Flask, request
from threading import Thread
import json
import telegrambot  # Pastikan modul telegrambot sudah diimpor atau didefinisikan

app = Flask('')


@app.route('/webhook', methods=['POST', 'GET'])
def get_webhook():
    try:
        jsonRequest = request.args.get("jsonRequest")
        if request.method == 'POST':
            payload = request.data
            if jsonRequest == "true":
                payload = json.loads(request.data)
                payload = json.dumps(payload, indent=4)
            else:
                payload = request.data.decode('utf-8')

            print("received data:\n", payload)
            telegrambot.sendMessage(payload)
            return 'success', 200
        else:
            print("Get request")
            return 'success', 200
    except Exception as e:
        print("[X] Exception Occurred:", e)
        return 'failure', 500


@app.route('/')
def main():
    # Assuming tradingview.login() is meant to be a function call related to tradingview
    # You can add your tradingview login logic here
    return 'Your bot is alive!'


def run():
    app.run(host='0.0.0.0', port=8080)


def start_server_async():
    server_thread = Thread(target=run)
    server_thread.start()


def start_server():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    start_server()
