from flask import Flask, request
from threading import Thread
import telegrambot
import json

app = Flask(__name__)


@app.route('/webhook', methods=['POST', 'GET'])
def get_webhook():
    try:
        json_request = request.args.get("jsonRequest")
        if request.method == 'POST':
            payload = request.data
            if json_request == "true":
                payload = json.dumps(request.json, indent=4)
                print("received data:\n", payload)
                telegrambot.send_message(payload)
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
    server = Thread(target=run)
    server.start()


def start_server():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    start_server_async()
