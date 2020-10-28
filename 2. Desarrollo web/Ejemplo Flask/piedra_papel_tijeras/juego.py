from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def inicio():
    fecha = date.today()
    return render_template(
        'selecciona_tiro.html',
        fecha=fecha)

@app.route('/tiro/<tiro_jugador>')
def tiro(tiro_jugador):
    tiro_compu = 'piedra'
    resultado = 1
    mensaje = f'{tiro_jugador} vence a {tiro_compu}'
    return render_template(
        'despliega_resultado.html',
        tiro_jugador=tiro_jugador,
        tiro_compu=tiro_compu,
        resultado=resultado,
        mensaje=mensaje)