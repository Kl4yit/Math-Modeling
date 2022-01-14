import numpy as np
import math


def fun_with_param(a, x):
    return (x - 1) ** 2 - math.e ** (-a * x)


def phi_with_param(a, x):
    # x - f(x)/f'(x)
    return x - fun_with_param(a, x)/derivative_fun_with_param(a, x)


def derivative_fun_with_param(a, x):
    return 2 * (x - 1) - (-a) * math.e ** (-a * x)


def derivative_phi_with_param(a, x):
    # не исправлял
    return 2 / (a * (x - 1))


def fun(x):
    return (x - 1) ** 2 - math.e ** -x


def phi(x):
    return x - fun_with_param(1, x)/derivative_fun_with_param(1, x)


def derivative_fun(x):
    return 2 * (x - 1) - math.e ** -x


def derivative_phi(x):
    return 2 / (x - 1)
