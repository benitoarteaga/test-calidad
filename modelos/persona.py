from app import db


class Persona(db.Model):
    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    carnet_identidad = db.Column(db.String(20), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    activo = db.Column(db.Boolean, default=True)

    redes_sociales = db.relationship('Asignacion', backref='persona', lazy=True)

    def __repr__(self):
        return f'<Persona {self.nombre} {self.apellidos}>'

    @staticmethod
    def listar():
        return Persona.query.all()

    @staticmethod
    def buscar(id):
        return db.session.get(Persona, id)

    @staticmethod
    def registrar(nombre, apellidos, carnet_identidad, correo, telefono, activo=True):
        nueva_persona = Persona(nombre=nombre, apellidos=apellidos, carnet_identidad=carnet_identidad, correo=correo,
                                telefono=telefono, activo=activo)

        db.session.add(nueva_persona)
        db.session.commit()
        return nueva_persona

    def modificar(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()