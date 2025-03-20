from flask import Flask, render_template
from producto import Producto


app = Flask(__name__)

@app.route('/')
def index():
    productos = [Producto("computadora", 200), Producto("impresora", 50)]
    return render_template('productos.html', productos=productos)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

 