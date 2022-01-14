import math


class Config:
    MIN = -4
    MAX = 2

    @staticmethod
    def our_function(x):
        return 1 / (1 + x**2)

    def __repr__(self):
        return '(1 + x^2)^-1'
