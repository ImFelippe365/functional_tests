import pytest
from src.triangle import Triangle

class TestBase:

    @pytest.fixture
    def setUp(self):
        side1 = int(input("Digite o 1º lado do triângulo: "))
        side2 = int(input("Digite o 2º lado do triângulo: "))
        side3 = int(input("Digite o 3º lado do triângulo: "))

        triangle = Triangle(side1, side2, side3)

        return triangle