
from flask import Flask

from flask import render_template, request

from model.ahorros import Ahorro

app = Flask(__name__)

@app.route('/')
def calcular_ahorro():
    meta = float( request.args["compra"] )
    meses = int( request.args["meses"] )
    abono = float( request.args["abono"] )
    intereses = float( request.args["intereses"] )

    result = Ahorro.""(meta, meses, abono, intereses)
    return f"Aqui se calcula el ahorro, la meta fue de {meta} a {meses} meses, con un abono de {abono}$ con una tasa de interes del {intereses}. para un ahorro mensual de {result}"

def hello():
    return render_template("ahorro.html")

if __name__ == '__main__':
    app.run( debug=True )
