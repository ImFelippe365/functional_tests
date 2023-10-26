from tests.test_base import TestBase

class TestIdentifier(TestBase):
    
    def test_all_sides_is_zero(self, setUp):
        assert setUp.all_sides_is_zero()
    
    def test_some_side_is_zero(self, setUp):
        assert setUp.some_side_is_zero()
    
    def test_all_sides_length(self, setUp):
        assert setUp.all_sides_length()
    
    def test_side_equals_sum_other(self, setUp):
        assert setUp.side_equals_sum_other()
