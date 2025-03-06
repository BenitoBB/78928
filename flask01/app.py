from flask import Flask

app = Flask(__name__)

@app.route('/') #lo vuelve aplicacion web
def hola_mundo():
    return 'Hola Mundo!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0',
debug=True)