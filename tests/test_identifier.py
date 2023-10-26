from tests.test_base import TestBase

class TestIdentifier(TestBase):
    
    def test_all_sides_is_zero(self, setUp):
        assert (setUp.side1 == 0 and setUp.side2 == 0 and setUp.side3 == 0)
    
    def test_some_side_is_zero(self, setUp):
        assert not (setUp.side1 == 0 or setUp.side2 == 0 or setUp.side3 == 0)
    
    def test_all_sides_length(self, setUp):
        allSidesSum = setUp.total_length / 2
        assert (setUp.side1 < allSidesSum and setUp.side2 < allSidesSum and setUp.side3 < allSidesSum)
    
    def test_side_equals_sum_other(self, setUp):
        allSidesSum = setUp.total_length / 2
        assert (setUp.side1 < allSidesSum and setUp.side2 < allSidesSum and setUp.side3 < allSidesSum)
