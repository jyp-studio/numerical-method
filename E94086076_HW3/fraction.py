from math import gcd

# you can change test values here
x_numerator, x_denominator = 1, 2
y_numerator, y_denominator = 2, 3


class Fraction(object):
    """
    User-defined ojbect to represent numeric fractions
    The top value, known as the numerator, can be any integer. 
    The bottom value, called the denominator, can be any integer 
    greater than 0 
    """

    def __init__(self, numerator: int, denominator: int, reduction: bool = False) -> None:
        '''initial fraction and do reduction if one requires'''
        # denominator cannot be 0
        if denominator != 0:
            self.numerator = int(numerator)
            self.denominator = int(denominator)
        # if reduction is true, reduce self-fraction
        if reduction:
            self.reduction()
        # check where is the negative sign
        self.__check_negative()

    def reciprocal(self) -> object:
        '''swap self.numerator and self.denominator'''
        tmp = self.numerator
        self.numerator = self.denominator
        self.denominator = tmp
        self.check_negative()
        return self

    def reduction(self) -> object:
        '''ruduce self-fraction'''
        self_gcd = gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / self_gcd)
        self.denominator = int(self.denominator / self_gcd)
        return self

    def __check_negative(self) -> object:
        '''make "-" sign only represent at self.numerator'''
        # if self.denominator is negative, swap "-" to self.numerator
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        return self

    def __gcd(self, other_fraction: object) -> int:
        '''return gcd of denominators'''
        gcd_denominator = gcd(self.denominator, other_fraction.denominator)
        return gcd_denominator

    def __add__(self, other_fraction: object) -> object:
        '''add two fractions'''
        # compare denominators of two fractions
        gcd_denominator = self.__gcd(other_fraction)
        # calculate denomination
        denominator = int(self.denominator *
                          other_fraction.denominator / gcd_denominator)
        # calculate numerator
        numerator = int(self.numerator * (other_fraction.denominator / gcd_denominator)
                        + other_fraction.numerator * (self.denominator / gcd_denominator))
        # reduce the fraction and return answer
        answer = Fraction(numerator, denominator, True)
        return answer

    def __sub__(self, other_fraction: object) -> object:
        '''subtract two fractions'''
        # as subtraction means adding negative other_fraction
        # that is, create a negative tmp fraction object of other_fraction
        tmp = Fraction(-other_fraction.numerator, other_fraction.denominator)
        return self.__add__(tmp)

    def __mul__(self, other_fraction: object) -> object:
        '''multiple two fractions'''
        numerator = self.numerator * other_fraction.numerator
        denominator = self.denominator * other_fraction.denominator
        # reduce the fraction and return answer
        answer = Fraction(numerator, denominator, True)
        return answer

    def __truediv__(self, other_fraction: object) -> object:
        '''div two fractions'''
        # since div means multipling the reciprocal of other_fraction
        tmp = Fraction(other_fraction.denominator, other_fraction.numerator)
        return self.__mul__(tmp)

    def __eq__(self, other_fraction: object) -> bool:
        '''check if two fractions are equal'''
        # reduce both fractions
        self_tmp = self.reduction()
        other_tmp = other_fraction.reduction()
        # return true if their values are same else return false
        return True if (self_tmp.numerator == other_tmp.numerator) \
            and (self_tmp.denominator == other_tmp.denominator) else False

    def __ne__(self, other_fraction: object) -> bool:
        '''check if two fractions are not equal'''
        # not equal means the opposite of equal
        # return false if their values are same else return true
        return False if self.__eq__(other_fraction) else True

    def __str__(self) -> str:
        if self.numerator == 0:  # if numerator is 0, return 0
            string = str(0)
        elif self.denominator == 1:  # else if denominator is 1, return numerator
            string = str(self.numerator)
        else:  # else return numerator/denominator
            string = f"{self.numerator}/{self.denominator}"
        return string

    def __repr__(self) -> str:
        if self.numerator == 0:  # if numerator is 0, return 0
            string = str(0)
        elif self.denominator == 1:  # else if denominator is 1, return numerator
            string = str(self.numerator)
        else:  # else return numerator/denominator
            string = f"{self.numerator}/{self.denominator}"
        return string


# test values
x = Fraction(x_numerator, x_denominator)
y = Fraction(y_numerator, y_denominator)
print("x + y =", x + y)
print("x == y ?", x == y)
print("x != y ?", x != y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
