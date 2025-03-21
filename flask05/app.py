from flask import Flask, render_template, request, Response, redirect, url_for
from producto import Producto
import sqlite3 

app = Flask(__name__)

#productos = [Producto("computadora", 200), Producto("impresora", 50)]

@app.route('/') #decorador
def index():
    con = conexion()
    productos = con.execute('SELECT * FROM productos').fetchall() # fetchall() trae todos los registros
    print(productos) # se imprime en consola, deberia imprimir []
    con.close()
    return render_template('productos.html', productos=productos)

@app.route('/editar/<id>') #Se le manda objeto producto y precio
def editar(id):
    con = conexion()
    p = con.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    con.close()
    return render_template('editar.html', producto=p) # Se declaran los objetos y se usan en el html

@app.route('/guardar', methods=['POST']) #Se le manda objeto producto y precio
def guardar():
    n = request.form.get('nombre')
    p = request.form.get('precio')
    id = request.form.get('id')
    print( f"nombre: {n} precio: {p}")
    con = conexion()
    con.execute('UPDATE productos SET nombre = ?, precio = ? WHERE id = ?', (n, p,id))
    con.commit()
    con.close()
    return Response("guardado", headers={'Location': '/'}, status=302)


@app.route('/eliminar/<id>')
def eliminar(id):
    con = conexion()
    con.execute('DELETE FROM productos WHERE id = ?', (id))
    con.commit()
    con.close()
    return Response("Eliminado", headers={'Location': '/'}, status=302)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    precio = request.form.get('precio')
    #productos.append(Producto(nombre, precio))
    con = conexion() # se crea la conexion
    con.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (nombre, precio)) # se inserta en la tabla
    con.commit() # se guardan los cambios
    con.close() # se cierra la conexion
    return redirect(url_for('index')) 

def conexion():
    con = sqlite3.connect('basedatos.db')
    # row_factory:
    # hace que las consultas se vuelvan diccionarios 
    # seleccionar valores mediante el nombre de la columna
    # ['nombre_columna']
    con.row_factory = sqlite3.Row
    return con

def iniciar_db():
    con  = conexion()
    # se crea la tabla en caso de que no exista
    con.execute('''
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')

    con.commit() # se guardan los cambios, en caso que no se haga commit, se pierden los cambios
    con.close()

if __name__ == '__main__':
    iniciar_db() # se llama a la funcion para crear la tabla y conexion a la base de datos
    app.run(host='0.0.0.0', debug=True)

 