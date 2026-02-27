# routes.py
from app import app, db
from flask import Flask, render_template
import formularios
from models import Tarea

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', subtitulo="Actividad en grupo TAI")

@app.route('/sobrenosotros', methods =['GET', 'POST'])
def sobrenosotros():
    # formulario es variable
    formulario = formularios.FormAgregarTareas()
    if formulario.validate_on_submit() :
        nueva_tarea = Tarea(titulo = formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()
        print('se envio correctamente', formulario.titulo.data)
        return render_template('sobrenosotros.html', 
                               form = formulario, 
                               titulo = formulario.titulo.data )

    return render_template('sobrenosotros.html', form=formulario)

#METODO PARA CARGAR LAS TAREAS
@app.context_processor
def cargar_tareas():
    tareas = Tarea.query.all()
    return dict(tareas=tareas)