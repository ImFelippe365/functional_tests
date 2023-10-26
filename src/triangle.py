class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.total_length = side1 + side2 + side3

    def all_sides_is_zero(self):
        return (self.side1 == 0 and self.side2 == 0 and self.side3 == 0)
    
    def some_side_is_zero(self):
        return not (self.side1 == 0 or self.side2 == 0 or self.side3 == 0)
    
    def all_sides_length(self):
        allSidesSum = self.total_length / 2
        return (self.side1 < allSidesSum and self.side2 < allSidesSum and self.side3 < allSidesSum)
    
    def side_equals_sum_other(self):
        side1Sum = (self.total_length - self.side1)
        side2Sum = (self.total_length - self.side2)
        side3Sum = (self.total_length - self.side3)
        
        return (self.side1 == side1Sum or self.side2 == side2Sum or self.side3 == side3Sum)
    