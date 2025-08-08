"""
@author: << Muhammad Farhan Azmine >>
"""
__version__ = 1


class Rational:
    '''
    Initialize a new Rational object with value iNum/iDen stored in __numerator
    and __denominator variables.  Calls the reduce() method to put the fraction
    in lowest terms.
    '''

    def __init__(self, iNum, iDen):
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def setNumerator(self, n):
        self.__numerator = n
        self.reduce()

    def setDenominator(self, d):
        self.__denominator = d
        self.reduce()

    def isValid(self):
        if (self.__denominator != 0):
            return True
        else:
            return False

    def add(self, num2):
        common_denom = self.__denominator * num2.__denominator
        common_numer = (self.__numerator * num2.__denominator) + (self.__denominator * num2.__numerator)
        self.__numerator = common_numer
        self.__denominator = common_denom
        self.reduce()

    def sub(self, num2):
        common_denom = self.__denominator * num2.__denominator
        common_numer = (self.__numerator * num2.__denominator) - (num2.__numerator * self.__denominator)
        self.__numerator = common_numer
        self.__denominator = common_denom
        self.reduce()

    def mult(self, num2):
        common_denom = self.__denominator * num2.__denominator
        common_numer = self.__numerator * num2.__numerator
        self.__numerator = common_numer
        self.__denominator = common_denom
        self.reduce()

    def div(self, num2):
        common_numer = self.__numerator * num2.__denominator
        common_denom = self.__denominator * num2.__numerator
        self.__numerator = common_numer
        self.__denominator = common_denom
        self.reduce()

        ################################

    #    HELPER FUNCTIONS BELOW    #
    ################################
    '''
    Reduces the Rational to lowest terms
      - Checks if both the numerator and denominator are negative; if so, makes both positive
      - Calls gcf() to find the greatest common factor between the numerator and denominator, and
        continues to divide by that gcf until the greatest common factor is 1
    '''

    def reduce(self):
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common

    '''
    Determines the greatest common factor between the numerator and denominator
      - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
      - When it finds a number divisble by both, it breaks the loop and returns that number
      - The smallest number that can be returned is 1
    '''

    def gcf(self):
        common_factor = 1
        for i in range(min(abs(int(self.__numerator)), abs(int(self.__denominator))), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                common_factor = i
                break
        return common_factor

    '''
    Returns a string representation of the Rational, e.g. "1/8"
    '''

    def __str__(self):
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))

    '''
    Determines if two Rationals are exactly equal to each other (same numerator and same
    denominator, no consideration of reducing the numbers)
    '''

    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator

    ################################
    #     END HELPER FUNCTIONS     #
    ################################


def main():
    # You can call test cases of your own here
    a=Rational(-14,-2)
    print(a)
    print(a.getNumerator())
    print(a.getDenominator())
    a.setDenominator(4)
    print(a)
    a.setNumerator(1)
    a.setDenominator(4)
    print(a)
    print(a.isValid())
    b=Rational(1,8)
    a.add(b)
    print(a)
    a.setNumerator(1)
    a.setDenominator(4)
    c=Rational(1,8)
    a.sub(c)
    print(a)
    a.setDenominator(4)
    a.mult(c)
    print(a)
    a.div(c)
    print(a)
###############################################################

if __name__ == "__main__":
    main()