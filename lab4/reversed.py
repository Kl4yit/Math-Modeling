from utils import *



def reversed_functions(a, b):
    if a > b:
        print("Данные некорректны")
        raise SystemExit(1)
    r = get_random_variable(3000)
    x = []
    for xi in r:
        xr = reverse_fun(xi, a, b)
        x.append(xr)
    x = bubble_sort(x)
    interval = [a, b]
    return x, interval
