from db import db

class Estudiante(db.Model):

    #Nombre de tabla

    __table__name__="estudiante"

    #Conjunto de atributos que van a ser loa campos de la tabla

    #Llave primaria
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    email=db.Column(db.String(70))
    codigo=db.Column(db.String(15))

    #Método constructor para mapear datos a los campos definidos

    def __initi__(self, nombre, email, codigo):

        self.nombre=nombre
        self.email=email
        self.codigo=codigo