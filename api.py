from flask import Flask, render_template, request
from PLN import analisis_texto 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludo', methods=['POST'])
def hola():
    intencion = request.form['nombre']
    
    resultado = analisis_texto(intencion)
    mensaje = f' {intencion}! Resultado del procesamiento: {resultado}'

    return render_template('saludo.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
