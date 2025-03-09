from tests import BaseTestCase, app
from modelos.persona import Persona, db
from modelos.red_social import RedSocial
from modelos.asignacion import Asignacion


class TestAsignacionModel(BaseTestCase):

    def test_registrar_asignacion(self):
        with app.app_context():
            persona = Persona.registrar("Sofia", "Martinez", "99887766", "sofia.martinez@example.com", "555555555", True)
            red_social = RedSocial.registrar("Snapchat", "Mi Snapchat", "https://snapchat.com/miperfil",
                                             "miemail@snapchat.com", "miperfil", "password123")
            asignacion = Asignacion.registrar(persona_id=persona.id, red_social_id=red_social.id,
                                              observacion="Primera asignación")
            self.assertIsNotNone(asignacion.id)
            self.assertEqual(asignacion.observacion, "Primera asignación")

    def test_listar_asignaciones(self):
        with app.app_context():
            persona = Persona.registrar("Julian", "Cruz", "44556677", "julian.cruz@example.com", "111222333", True)
            red_social = RedSocial.registrar("Pinterest", "Mi Pinterest", "https://pinterest.com/miperfil",
                                             "miemail@pinterest.com", "miperfil", "password123")
            Asignacion.registrar(persona_id=persona.id, red_social_id=red_social.id)
            asignaciones = Asignacion.listar()
            self.assertGreaterEqual(len(asignaciones), 1)

    def test_buscar_asignacion(self):
        with app.app_context():
            persona = Persona.registrar("Laura", "Diaz", "33445566", "laura.diaz@example.com", "777888999", True)
            red_social = RedSocial.registrar("Tumblr", "Mi Tumblr", "https://tumblr.com/miperfil", "miemail@tumblr.com",
                                             "miperfil", "password123")
            asignacion = Asignacion.registrar(persona_id=persona.id, red_social_id=red_social.id)
            buscada = Asignacion.buscar(asignacion.id)
            self.assertIsNotNone(buscada)

    def test_modificar_asignacion(self):
        with app.app_context():
            persona = Persona.registrar("Luis", "Vega", "22334455", "luis.vega@example.com", "444555666", True)
            red_social = RedSocial.registrar("WhatsApp", "Mi WhatsApp", None, "miemail@whatsapp.com", "miperfil",
                                             "password123")
            asignacion = Asignacion.registrar(persona_id=persona.id, red_social_id=red_social.id)
            asignacion.modificar(observacion="Modificado")
            self.assertEqual(asignacion.observacion, "Modificado")

    def test_eliminar_asignacion(self):
        with app.app_context():
            persona = Persona.registrar("Esteban", "Sanchez", "55667788", "esteban.sanchez@example.com", "888999000", True)
            red_social = RedSocial.registrar("TikTok", "Mi TikTok", "https://tiktok.com/miperfil", "miemail@tiktok.com",
                                             "miperfil", "password123")
            asignacion = Asignacion.registrar(persona_id=persona.id, red_social_id=red_social.id)
            asignacion_id = asignacion.id
            asignacion.eliminar()
            self.assertIsNone(Asignacion.buscar(asignacion_id))
