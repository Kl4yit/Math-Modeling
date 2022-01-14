import numpy as np
from matplotlib import pyplot as plt
from config import Config


def plot_graphic():
    a, b, func = Config.interval_start, Config.interval_end, Config.our_function
    x = np.linspace(a, b, 1000)
    plt.plot(x, [func(i) for i in x])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Целевая функция')
    plt.show()
