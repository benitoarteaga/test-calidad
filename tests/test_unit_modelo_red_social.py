from tests import BaseTestCase, app
from modelos.red_social import RedSocial


class TestRedSocialModel(BaseTestCase):

    def test_registrar_red_social(self):
        with app.app_context():
            red_social = RedSocial.registrar(
                tipo_red_social="Facebook",
                nombre="Mi Facebook",
                url="https://facebook.com/miperfil",
                correo="miemail@facebook.com",
                usuario="miperfil",
                contrasena="password123"
            )
            self.assertIsNotNone(red_social.id)
            self.assertEqual(red_social.tipo_red_social, "Facebook")

    def test_listar_redes_sociales(self):
        with app.app_context():
            RedSocial.registrar("Instagram", "Mi Instagram", "https://instagram.com/miperfil", "miemail@instagram.com",
                                "miperfil", "password123")
            redes_sociales = RedSocial.listar()
            self.assertGreaterEqual(len(redes_sociales), 1)

    def test_buscar_red_social(self):
        with app.app_context():
            red = RedSocial.registrar("Twitter", "Mi Twitter", "https://twitter.com/miperfil", "miemail@twitter.com",
                                      "miperfil", "password123")
            buscada = RedSocial.buscar(red.id)
            self.assertIsNotNone(buscada)
            self.assertEqual(buscada.nombre, "Mi Twitter")

    def test_modificar_red_social(self):
        with app.app_context():
            red = RedSocial.registrar("LinkedIn", "Mi LinkedIn", "https://linkedin.com/miperfil", "miemail@linkedin.com",
                                      "miperfil", "password123")
            red.modificar(url="https://linkedin.com/nuevo_perfil")
            self.assertEqual(red.url, "https://linkedin.com/nuevo_perfil")

    def test_eliminar_red_social(self):
        with app.app_context():
            red = RedSocial.registrar("YouTube", "Mi YouTube", "https://youtube.com/miperfil", "miemail@youtube.com",
                                      "miperfil", "password123")
            red_id = red.id
            red.eliminar()
            self.assertIsNone(RedSocial.buscar(red_id))