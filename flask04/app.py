from flask import Flask, render_template
from producto import Producto
from flask import request
from flask import Response

app = Flask(__name__)

productos = [Producto("computadora", 200), Producto("impresora", 50)]

@app.route('/') #decorador
def index():
    #productos = [Producto("computadora", 200), Producto("impresora", 50)]
    return render_template('productos.html', productos=productos)

@app.route('/editar/<producto>/<precio>') #Se le manda objeto producto y precio
def editar(producto, precio):
    # Recuperar el producto a editar    
    return render_template('editar.html', producto=producto, precio=precio) # Se declaran los objetos y se usan en el html
    # primero es el html y luego los objetos

@app.route('/guardar', methods=['POST']) #Se le manda objeto producto y precio
def guardar():
    n = request.form.get('nombre')
    p = request.form.get('precio')
    print (n,p)
    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i].precio = Producto(n, p)
            print (f"{e.nombre} {e.precio}")
        i += 1  
    return Response("guardado", headers={'Location': '/'}, status=302)


@app.route('/eliminar/<nombre>', methods=['POST'])
def eliminar(nombre):
    global productos
    # Filtrar la lista para eliminar el producto con el nombre especificado
    productos = [p for p in productos if p.nombre != nombre]
    print(f"Producto eliminado: {nombre}")
    return Response("Eliminado", headers={'Location': '/'}, status=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

 