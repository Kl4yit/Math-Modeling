from text import gauss_text
from utils import *


def gaussian_sampling():
    m_gauss, d_gauss = gauss_text()
    sigma = math.sqrt(d_gauss)
    n = 6
    x = []
    for i in range(1000):
        v = 0
        for j in range(n):
            v += rnd.random()
        xi = fun_gauss(v, m_gauss, sigma, n)
        x.append(xi)
    x = bubble_sort(x)
    interval = [x[0], x[-1]]
    return [x, interval, m_gauss, d_gauss]

