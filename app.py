# app.py
from flask import Flask
from rutas import ruta

app = Flask(__name__)
app.register_blueprint(ruta)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)