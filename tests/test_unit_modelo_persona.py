from tests import BaseTestCase, app
from modelos.persona import Persona


class TestUnitModeloPersona(BaseTestCase):

    def test_registrar_persona(self):
        with app.app_context():
            persona = Persona.registrar(
                nombre="Juan",
                apellidos="Pérez",
                carnet_identidad="12345678",
                correo="juan.perez@example.com",
                telefono="123456789",
                activo=True
            )
            self.assertIsNotNone(persona.id)
            self.assertEqual(persona.nombre, "Juan")
            self.assertEqual(persona.apellidos, "Pérez")

    def test_listar_personas(self):
        with app.app_context():
            Persona.registrar("Roberto", "Pérez", "12345699", "roberto.perez@example.com", "76042140", True)
            personas = Persona.listar()
            self.assertGreaterEqual(len(personas), 1)

    def test_buscar_persona(self):
        with app.app_context():
            persona = Persona.registrar("Carlos", "Gomez", "87654321", "carlos.gomez@example.com", "987654321", True)
            buscada = Persona.buscar(persona.id)
            self.assertIsNotNone(buscada)
            self.assertEqual(buscada.nombre, "Carlos")

    def test_modificar_persona(self):
        with app.app_context():
            persona = Persona.registrar("Maria", "Lopez", "13579246", "maria.lopez@example.com", "246813579", True)
            persona.modificar(nombre="Maria Jose", telefono="999888777")
            self.assertEqual(persona.nombre, "Maria Jose")
            self.assertEqual(persona.telefono, "999888777")

    def test_eliminar_persona(self):
        with app.app_context():
            persona = Persona.registrar("Ana", "Garcia", "11223344", "ana.garcia@example.com", "998877665", True)
            persona_id = persona.id
            persona.eliminar()
            self.assertIsNone(Persona.buscar(persona_id))

