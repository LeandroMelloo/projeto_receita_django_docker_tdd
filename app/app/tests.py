from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):
    def test_add_numbers(self):
       """Teste para validar a entrada de 2 numeros"""
       self.assertEqual(add(3,8), 11)
       
    def test_subtract_numbers(self):
        """Teste de valores subtraidos e retornados"""
        self.assertEqual(subtract(11,5), 6)