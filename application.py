import os
from flask import Flask, render_template, request, session
from flask_session import Session
from conexionDB import conectorDB
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
listaNotas = []
app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
conexionDB = conectorDB()

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

@app.route('/notas', methods = ['GET', 'POST'])
def notas():
    if session.get('notas') is None:
        session['notas'] = []
    if request.method == 'POST':
        nota = request.form.get('nota')
        #listaNotas.append(nota)
        if nota != '' and nota != ' ':
            if nota == '##borrar##':
                session['notas'] = []
            else:
                session['notas'].append(nota)
    
    return render_template('notas.html', notas = session['notas'], headline = 'Notas')
