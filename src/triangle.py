class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.total_length = side1 + side2 + side3

    def is_valid(self):
        if self.side1 < 1 or self.side2 < 1 or self.side3 < 1:
            return False

        return True