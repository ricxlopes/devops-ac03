import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    primos = ""
    n = 0
    x = 0

    while(n < 100):
        if eh_primo(x):
            primos += str(x) + " "
            n += 1

        x += 1
    return primos


def eh_primo(n):
    for x in range(2, n):
        if not n % x:
            return False
    return True


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
