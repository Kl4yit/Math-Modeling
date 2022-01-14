import math
import random as rnd
import matplotlib.pyplot as plt


def reverse_fun(ri, ai, bi):
    return (ri * (bi - ai)) + ai


def get_random_variable(size):
    arr = []
    for i in range(size):
        arr.append(rnd.random())
    return arr


def bubble_sort(a):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def fun_gauss(v, m, sigma, N):
    el = math.sqrt(12 / N) * (v - (N / 2))
    return sigma * el + m


def rayleigh_distribution(xl, sigma):
    return (xl / (sigma ** 2)) * math.exp(-1 * ((xl ** 2) / (2 * (sigma ** 2))))


def fn_normal(a, b, x):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0


def f_normal(a, b, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif x >= b:
        return 1
    else:
        return 0


def fn_gauss(x, m, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-1 * (x - m) ** 2 / (2 * (sigma ** 2)))


def f_gauss(x, m, sigma):
    return (1 / 2) * (1 + math.erf((x - m) / math.sqrt(2 * (sigma ** 2))))


def fn_rayleigh(x, sigma):
    return (x / (sigma ** 2)) * math.exp(-1 * ((x ** 2) / (2 * (sigma ** 2))))


def f_rayleigh(x, sigma):
    return 1 - math.exp(-1 * (x ** 2) / (2 * sigma ** 2))


def plot_density_fn(X, a, b, dstr, m=0, d=0, sigma=0):
    if dstr == 1:
        r = []
        for x in X:
            r.append(fn_normal(a, b, x))
        plt.plot(X, r)
    elif dstr == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(fn_gauss(x, m, sigma))
        plt.plot(X, r)
    elif dstr == 3:
        r = []
        for x in X:
            r.append(fn_rayleigh(x, sigma))
        plt.plot(X, r)


def plot_density_f(X, a, b, dstr, m=0, d=0, sigma=0):
    if dstr == 1:
        r = []
        for x in X:
            r.append(f_normal(a, b, x))
        plt.plot(X, r)
    elif dstr == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(f_gauss(x, m, sigma))
        plt.plot(X, r)
    elif dstr == 3:
        r = []
        for x in X:
            r.append(f_rayleigh(x, sigma))
        plt.plot(X, r)


def find_mathematical_expectation(X):
    s = 0
    for x in X:
        s += x
    return s / len(X)


def find_dispersion(X, m):
    s = 0
    for x in X:
        s += (x - m)**2
    return s / len(X)
