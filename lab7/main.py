import matplotlib.pyplot as plt
import numpy as np

from dichotomy_method import dichotomy_method_with_param
from functions import fun_with_param, fun
from hord_method import hord_method_with_params
from newton_method import newton_method_with_param
from iteration_method import iteration_method_with_param


def create_plot(x, y1, title):
    plt.title(title)
    plt.plot(x, y1)
    plt.grid(True)
    plt.show()


# Вводим начальные значения
a = float(input("Параметр a: "))


x = np.linspace(-0.2, 0.3, 1000)

y1 = fun_with_param(a,  x)
y2 = fun(x)

plt.plot(x, y1)
plt.title("Функция уравнения f(x)")
plt.grid(True)
plt.show()

intervalA = float(input("Левая граница: "))
intervalB = float(input("Правая граница: "))

x0 = float(input("Начальное приближение x: "))
eps = 0.001


s = str(eps)
number = abs(s.find('.') - len(s)) - 1

n = int(input("Число итераций n: "))
print("-----------------------------------------------")

dichotomy_method_with_param(eps, number, a, intervalA, intervalB)
create_plot(x, y1, "Метод дихотомии")


iteration_method_with_param(x0, eps, number, a)
create_plot(x, y1, "Метод простых итераций")


newton_method_with_param(x0, n, a, eps, number)
create_plot(x, y1, "Метод Ньютона")


hord_method_with_params(x0, n, a, eps, number, intervalA, intervalB)
create_plot(x, y1,  "Метод хорд")
