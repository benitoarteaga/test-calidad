from datetime import datetime
from app import db


class Asignacion(db.Model):
    __tablename__ = 'asignaciones'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    red_social_id = db.Column(db.Integer, db.ForeignKey('redes_sociales.id'), nullable=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'), nullable=False)
    fecha_asignacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_finalizacion = db.Column(db.DateTime, nullable=True)
    activo = db.Column(db.Boolean, default=True)
    observacion = db.Column(db.String(255), nullable=True)

    @staticmethod
    def listar():
        return Asignacion.query.all()

    @staticmethod
    def buscar(id):
        return db.session.get(Asignacion, id)

    @staticmethod
    def registrar(red_social_id, persona_id, fecha_asignacion=None, fecha_finalizacion=None, activo=True,
                  observacion=""):
        nueva_asignacion = Asignacion(red_social_id=red_social_id, persona_id=persona_id,
                                      fecha_asignacion=fecha_asignacion or datetime.utcnow(),
                                      fecha_finalizacion=fecha_finalizacion, activo=activo, observacion=observacion)
        db.session.add(nueva_asignacion)
        db.session.commit()
        return nueva_asignacion

    def modificar(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()
