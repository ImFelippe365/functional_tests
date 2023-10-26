import pytest
from src.triangle import Triangle

class TestBase:

    @pytest.fixture
    def setUp(self):
        # triangle = Triangle(0,0,0)
        # triangle = Triangle(10,5,0)
        # triangle = Triangle(8,8,8)
        triangle = Triangle(4,2,2)

        return triangle