from fractions import Fraction

class Rational:

    def __init__(self, firstnum, secondnum):
        if ((isinstance(firstnum, int) == False and isinstance(firstnum, float) == False) or
                (isinstance(secondnum, int) == False and isinstance(secondnum, float) == False)):
            raise Exception("Both arguments have to be rational numbers")
        self.first = firstnum
        self.second = secondnum

    def add(self):
        return Fraction(self.first + self.second).limit_denominator()

    def subtract(self):
        return Fraction(self.first - self.second).limit_denominator()

    def multiply(self):
        return Fraction(self.first * self.second).limit_denominator()

    def divide(self):
        return Fraction(self.first / self.second).limit_denominator()

    def compare(self):
        if self.first > self.second:
            return f'{self.first} > {self.second}'
        elif self.first < self.second:
            return f'{self.first} < {self.second}'
        else:
            return f'{self.first} = {self.second}'


if __name__ == '__main__':
    obj1 = Rational(3.4, 0.3)
    print(obj1.add())
    print(obj1.subtract())
    print(obj1.multiply())
    print(obj1.divide())
    print(obj1.compare(), '\n')
    obj2 = Rational(4.4, 13.2)
    print(obj2.add())
    print(obj2.subtract())
    print(obj2.multiply())
    print(obj2.divide())
    print(obj2.compare(), '\n')




