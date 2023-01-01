from fractions import Fraction

class Rational:

    def __init__(self, num):
        self.number = num

    def __add__(self, obj):
        return Fraction(self.number + obj.number).limit_denominator()

    def __sub__(self, obj):
        return Fraction(self.number - obj.number).limit_denominator()

    def __mul__(self, obj):
        return Fraction(self.number * obj.number).limit_denominator()

    def __truediv__(self, obj):
        return Fraction(self.number / obj.number).limit_denominator()

    def __gt__(self, obj):
        if self.number > obj.number:
            return True
        return False


if __name__ == '__main__':
    obj1 = Rational(5.4)
    obj2 = Rational(0.9)
    print(obj1 + obj2)
    print(obj1 - obj2)
    print(obj1 * obj2)
    print(obj1 / obj2)
    print(obj1 > obj2)
    print(obj1 < obj2)
