import math
from abc import ABCMeta, abstractmethod
from random import random

from scipy import integrate

from config import Config
from math_utils import generate_random_variables, get_function_max


class AbstractIntegration(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def count(N):
        pass


class Analytical(AbstractIntegration):

    @staticmethod
    def count(N: int = 100):
        return math.atan(2) - math.atan(-4)


class Trapezium(AbstractIntegration):

    @staticmethod
    def count(N: int = 100):
        a, b, func = Config.MIN, Config.MAX, Config.our_function
        h = (b - a) / N
        s = 0
        while round(a, 8) < b:
            s += 0.5 * h * (func(a) + func(a + h))
            a += h
        return s

    def __str__(self):
        return 'Trapezium method'


class MonteCarloFirst(AbstractIntegration):

    @staticmethod
    def count(N: int = 100):
        a, b, func = Config.MIN, Config.MAX, Config.our_function
        SUM = 0
        random_values = generate_random_variables(N)
        for i in range(N):
            U = random_values[i] * (b - a) + a
            SUM += func(U)

        return (b - a) / N * SUM

    def __str__(self):
        return 'Monte-Carlo 1st method'


class MonteCarloSecond(AbstractIntegration):

    @staticmethod
    def count(N: int = 128):
        a, b, func = Config.MIN, Config.MAX, Config.our_function
        k = 0
        difference, min_value = get_function_max(N)
        for i in range(N):
            X = a + (b - a) * random()
            Y = (min_value + difference) * random()
            if 0 < Y < func(X):
                k += 1

        return difference * (b - a) * k / N

    def __str__(self):
        return 'Monte-Carlo 2nd method'
