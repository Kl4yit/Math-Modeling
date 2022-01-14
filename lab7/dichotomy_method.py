import matplotlib.pyplot as plt

from functions import fun_with_param, fun


def dichotomy_method_with_param(eps, number, a, intervalA, intervalB):
    root = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        n += 1
        if fun_with_param(a, root) == 0:
            break
        if fun_with_param(a, intervalA) * fun_with_param(a, root) < 0:
            intervalB = root
        elif fun_with_param(a, intervalB) * fun_with_param(a, root) < 0:
            intervalA = root
        root = (intervalB + intervalA) / 2
    print("Метод дихотомии X: ", round(root, number))
    print("Число итераций в методе дихотомии: ", n)
    print("-----------------------------------------------")
    y = fun_with_param(a, root)
    plt.scatter(root, y, color="red")


def dichotomy_method_without_param(eps, number, intervalA, intervalB):
    root = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        n += 1
        if fun(root) == 0:
            break
        if fun(intervalA) * fun(root) < 0:
            intervalB = root
        elif fun(intervalB) * fun(root) < 0:
            intervalA = root
        root = (intervalB + intervalA) / 2
    print("Число итераций: ", n)
    print("Без параметров: ", round(root, number))
