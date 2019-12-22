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
listaPaginas = ['tradicionales', 'exoticas', 'pan', 'notas']
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
def contenido(name = 'defecto'):
    if name in listaPaginas:
        listaAux = listaPaginas.copy()
        listaAux.remove(name)
        """
        for i in listaPaginas:
            if i != name:
                listaAux.append(i)
        """        
        return render_template('contenido.html', headline = name, listaPaginas = listaAux)
    else:
        return render_template('default_error.html', headline = 'Pagina %s desconocida' % name)

@app.route('/notas', methods = ['GET', 'POST'])
def notas():
    listaAux = listaPaginas.copy()
    listaAux.remove('notas')
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
    
    return render_template('notas.html', notas = session['notas'], headline = 'Notas', listaPaginas = listaAux)


if __name__ == '__main__':
    app.run('0.0.0.0')