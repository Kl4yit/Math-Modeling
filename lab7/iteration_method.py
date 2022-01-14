import matplotlib.pyplot as plt

from functions import fun_with_param, phi_with_param, phi


def iteration_method_with_param(x0, eps, number, a):

    root = phi_with_param(a, x0)
    x = x0
    n = 0
    while abs(root - x) >= eps:
        n += 1
        x = root
        root = phi_with_param(a, x)
    print("Метод простых итераций. X: ", round(
        root, number))
    print("Число итераций в методе простых итераций: ", n)
    print("-----------------------------------------------")
    y = fun_with_param(a, root)
    plt.scatter(root, y, color="red")


def iteration_method_without_param(x, eps, number):
    root = phi(x)
    n = 0
    while abs(root - x) >= eps:
        n += 1
        x = root
        root = phi(x)
    print("Число итераций: ", n)
    print("Без параметров: ", round(root, number))
