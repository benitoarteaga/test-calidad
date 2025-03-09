from app import db


class RedSocial(db.Model):
    __tablename__ = 'redes_sociales'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_red_social = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(255), nullable=True)
    correo = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

    asignaciones = db.relationship('Asignacion', backref='red_social', lazy=True)

    @staticmethod
    def listar():
        return RedSocial.query.all()

    @staticmethod
    def buscar(id):
        return db.session.get(RedSocial, id)

    @staticmethod
    def registrar(tipo_red_social, nombre, url, correo, usuario, contrasena):
        nueva_red = RedSocial(tipo_red_social=tipo_red_social, nombre=nombre, url=url, correo=correo, usuario=usuario, contrasena=contrasena)
        db.session.add(nueva_red)
        db.session.commit()
        return nueva_red

    def modificar(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()