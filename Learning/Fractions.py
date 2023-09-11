class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    
    def toFloat(self):
        return float(self.numerator / self.denominator)
    
    def invert(self):
        number = self.numerator
        self.numerator = self.denominator
        self.denominator = number
        return  self
    
    def __add__(self,other):
        return Fraction(self.numerator+other.numerator,self.denominator+other.denominator)

    def __sub__(self,other):
        return Fraction(self.numerator-other.numerator,self.denominator-other.denominator)
    
    def __mul__(self,other):
        return Fraction(self.numerator*other.numerator,self.denominator*other.denominator)
    
    def __truediv__(self,other):
        return Fraction(self.numerator/other.numerator,self.denominator/self.denominator)