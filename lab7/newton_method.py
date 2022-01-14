import matplotlib.pyplot as plt

from functions import fun_with_param, derivative_fun_with_param, fun, derivative_fun


def newton_method_with_param(x, n, a, eps, number):
    root = x
    N = 0
    for i in range(n):
        N += 1
        root = x - (fun_with_param(a, x) /
                    derivative_fun_with_param(a, x))
        if abs(root - x) < eps:
            break
        x = root
    print("Метод Ньютона X: ", round(root, number))
    print("Число итераций в методе Ньютона: ", N)
    print("-----------------------------------------------")
    y = fun_with_param(a, root)
    plt.scatter(root, y, color="red")


def newton_method_without_param(x, n, eps, number):
    root = x
    N = 0
    for i in range(n):
        N += 1
        root = x - (fun(x) / derivative_fun(x))
        if abs(root - x) < eps:
            break
        x = root
    print("Число итераций: ", N)
    print("Без параметров: ", round(root, number))
