from flask import Flask, render_template, request
"""
    Ayuda sintaxis:
    {{ variable }}
    
    {% if True %}
    {% else %}
    {% endif %}

    {% for variable in variabels %}
    {% endfor %}

    {{ url_for('index') }}

    {% extends 'plantilla.html' %}
    
    {% block nombreDelBloque %}
    {% endblock nombreDelBloque %}
"""
listaPaginas = ['tradicionales', 'exoticas', 'pan']
app = Flask(__name__)

@app.route('/')
def index():
    headline = 'Bienvenido a mi pagina'
    #return render_template('index.html')
    return render_template('index.html', headline = headline, listaPaginas = listaPaginas)

@app.route('/<string:name>')
def paginaDefault(name = 'defecto'):
    print(name)
    if name in listaPaginas:
        return render_template('contenido.html', headline = name)
    else:
        return render_template('default_error.html', headline = 'Pagina %s desconocida' % name)
