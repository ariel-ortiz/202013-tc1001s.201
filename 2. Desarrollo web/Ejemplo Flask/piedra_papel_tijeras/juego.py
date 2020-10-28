from flask import Flask, render_template
from datetime import date
from random import choice

app = Flask(__name__)

reglas = {
    'piedra': {
        'piedra':  {'resultado': 0,  'mensaje': 'Empate'},
        'papel':   {'resultado': -1, 'mensaje': 'Papel envuelve piedra'},
        'tijeras': {'resultado': 1,  'mensaje': 'Piedra aplasta tijeras'}
    },
    'papel': {
        'piedra':  {'resultado': 1,  'mensaje': 'Papel envuelve piedra'},
        'papel':   {'resultado': 0,  'mensaje': 'Empate'},
        'tijeras': {'resultado': -1, 'mensaje': 'Tijeras cortan papel'}
    },
    'tijeras': {
        'piedra':  {'resultado': -1, 'mensaje': 'Piedra aplasta tijeras'},
        'papel':   {'resultado': 1,  'mensaje': 'Tijeras cortan papel'},
        'tijeras': {'resultado': 0,  'mensaje': 'Empate'},
    }
}

objetos = list(reglas.keys())

@app.route('/')
def inicio():
    fecha = date.today()
    return render_template(
        'selecciona_tiro.html',
        fecha=fecha)

@app.route('/tiro/<tiro_jugador>')
def tiro(tiro_jugador):
    tiro_compu = choice(objetos)
    resultado = reglas[tiro_jugador][tiro_compu]['resultado']
    mensaje = reglas[tiro_jugador][tiro_compu]['mensaje']
    return render_template(
        'despliega_resultado.html',
        tiro_jugador=tiro_jugador,
        tiro_compu=tiro_compu,
        resultado=resultado,
        mensaje=mensaje)