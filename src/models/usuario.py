from config.bd import db, ma, app
import mysql.connector
class usuario (db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70))
    clave =db.Column(db.String(70))

    def __init__(self,nombre,clave):
        self.nombre= nombre
        self.clave= clave
conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")

with app.app_context():
    db.create_all()

    class usuarioSchema (ma.Schema):
        class meta:
            fields=('id','nombre','clave')
