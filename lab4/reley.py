from text import reley_text
from utils import *
from reversed import reversed_functions


def reley_sampling():
    len_r = 3000
    sigma, b = reley_text()
    max_y = rayleigh_distribution(sigma, sigma)
    rj = get_random_variable(len_r)
    ri = get_random_variable(len_r)
    x = []
    i = 1
    while i <= len_r:
        X = 4 * sigma * rj[i - 1]
        Y = max_y * rj[i]
        if Y < rayleigh_distribution(X, sigma):
            x.append(X)
        i += 1
        if len(x) >= 1000:
            break
    x = bubble_sort(x)
    interval = [0, x[-1]]
    return [x, interval, sigma]


