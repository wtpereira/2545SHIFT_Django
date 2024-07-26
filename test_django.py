from django.test import TestCase
from gestao.models import Autor

class AutorTestCase(TestCase):
    def setUp(self) -> None:
        Autor.objects.create(nome='Machado de Assis', email='machado@assis.com')
        Autor.objects.create(nome='Paulo Coelho', email='pauco@coelho.com')

    def test_autores(self):
        machado = Autor.objects.get(nome='Machado de Assis')
        paulo = Autor.objects.get(nome='Paulo Coelho')

        self.assertEqual(machado.email, 'machado@assis.com')
        self.assertEqual(paulo.email, 'pauco@coelho.com')
