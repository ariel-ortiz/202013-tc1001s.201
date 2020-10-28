from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def inicio():
    fecha = date.today()
    return render_template(
        'selecciona_tiro.html',
        fecha=fecha)