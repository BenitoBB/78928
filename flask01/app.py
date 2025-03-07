from flask import Flask

app = Flask(__name__)

@app.route('/saludar') #lo vuelve aplicacion web
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/despedir') #otro tipo de ruta o "directorio"
def adios_mundo():
    return 'Adios Mundo!'

@app.route('/hola') 
def hola_html():
    return '<h1 style="color:red">HOLA</h1>'

@app.route('/json')
def algo():
    return '{"nombre":"benito"}'

@app.route('/xml')
def xml():
    return '<?xml version="1.0"?>  <nombre>Benito</nombre>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
