from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route('/saludar')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/despedir')
def adios_mundo():
    return 'Adios Mundo!'

@app.route('/hola') 
def hola_html():
    return '<h1 style="color:red">HOLA</h1>'

@app.route('/json')
def json_response():
    return jsonify({"nombre": "Benito"})

@app.route('/xml')
def xml_response():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <persona>
        <nombre>Benito</nombre>
        <apellido>Camelo</apellido>
    </persona>'''
    return Response(xml, mimetype='application/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
