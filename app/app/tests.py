from django.test import SimpleTestCase
from .calculation import addition, subtraction, divide


class TestCalculation(SimpleTestCase):

    def test_calculation(self):

        result = addition(10, 5)

        self.assertEqual(result, 15)


class TestSubtraction(SimpleTestCase):
    def test_subtraction(self):
        res = subtraction(5, 3)
        self.assertEqual(res, 2)


class TestDivision(SimpleTestCase):
    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
