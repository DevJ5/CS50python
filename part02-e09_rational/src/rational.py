#!/usr/bin/env python3


# p/q, where p and q are both integers and q ≠ 0.
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return f"{self.p}/{self.q}"

    def __add__(self, x):
        commonDenominator = self.q * x.q
        nom1 = self.p * x.q
        nom2 = x.p * self.q
        return Rational(nom1 + nom2, commonDenominator)

    def __sub__(self, x):
        commonDenominator = self.q * x.q
        nominator1 = self.p * x.q
        nominator2 = x.p * self.q
        return Rational(nominator1 - nominator2, commonDenominator)

    def __mul__(self, x):
        nominator = self.p * x.p
        denominator = self.q * x.q
        return Rational(nominator, denominator)

    def __truediv__(self, x):
        nominator = self.p * x.q
        denominator = self.q * x.p
        return Rational(nominator, denominator)

    def __eq__(self, x):
        commonDenominator = self.q * x.q
        nom1 = self.p * x.q
        nom2 = x.p * self.q
        return nom1 == nom2

    def __gt__(self, x):
        commonDenominator = self.q * x.q
        nom1 = self.p * x.q
        nom2 = x.p * self.q
        return nom1 > nom2

    def __lt__(self, x):
        commonDenominator = self.q * x.q
        nom1 = self.p * x.q
        nom2 = x.p * self.q
        return nom1 < nom2


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
