from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Aprendiendo Flask con Mario Alvarez"


@app.route('/informacion')
def informacion():
    return "<h1>Pagina de informacion</h1>"


@app.route('/contacto')
def contacto():
    return "<h1>Pagina de contacto</h1>"


@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Pagina de Lenguajes</h1>"


if __name__ == '__main__':
    app.run(debug=True)
