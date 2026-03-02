from flask import Flask
from extension import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/db_tareas"

db.init_app(app)

from models import Tarea
with app.app_context():
    db.create_all()

# Importamos las rutas al final para evitar errores
from routes import *

if __name__ == '__main__':
    app.run(debug=True)