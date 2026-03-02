from flask import render_template, redirect, url_for
from app import app
from extension import db
from models import Tarea
from formularios import FormAgregarTareas

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sobrenosotros', methods=['GET', 'POST'])
def sobrenosotros():
    form = FormAgregarTareas()
    if form.validate_on_submit():
        nueva = Tarea(titulo=form.titulo.data)
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('sobrenosotros'))
    
    tareas_db = Tarea.query.all()
    return render_template('sobrenosotros.html', form=form, tareas=tareas_db)

@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar(id):
    tarea = Tarea.query.get_or_404(id)
    form = FormAgregarTareas(obj=tarea) # Carga los datos actuales
    
    if form.validate_on_submit():
        tarea.titulo = form.titulo.data
        db.session.commit()
        return redirect(url_for('sobrenosotros'))
    
    return render_template('actualizar.html', form=form)

# Esto permite que la tabla funcione en cualquier página que use base.html
@app.context_processor
def inject_tareas():
    return dict(tareas=Tarea.query.all())