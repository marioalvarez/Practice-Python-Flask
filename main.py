from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Aprendiendo Flask con Mario Alvarez"


@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<string:apellido>')
def informacion(nombre=None, apellido=None):

    texto = ""
    if nombre != None and apellido != None:
        texto = f"<h3>Bienvenido, {nombre} {apellido}</h3>"

    return f"""
            <h1>Pagina de informacion</h1>
            <p>Esta es la pagina de información</p>
            {texto}
    """


@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion=None):

    if redireccion is not None:
        return redirect(url_for('lenguajes'))
    return "<h1>Pagina de contacto</h1>"


@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Pagina de Lenguajes</h1>"


if __name__ == '__main__':
    app.run(debug=True)
