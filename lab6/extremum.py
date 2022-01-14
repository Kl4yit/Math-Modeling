from config import Config
from golden_ratio import GoldenRatio
from fibbonachi import get_extremum_of_function_by_fibonacci_method


def find_extremum():
    print("Введите отрезок [a, b]")
    a, b = [value for value in
            list(map(int, input("(2 целых числа через пробел): ").split(' ')))]
    Config.interval_start = a
    Config.interval_end = b
    golden = GoldenRatio()
    print("Введите тип экстремума")
    print("1 - максимум")
    print("2 - минимум")
    extr_type = int(input('>>>'))
    print("Введите точность при нахождении экстремума")
    epsilon = float(input('>>>'))
    q = input('Вы хотите ввести число "n" итераций для метода фибоначчи [y/n]?\n>>>')
    if q == 'y':
        print('Введите число итераций "n" для метода Фибоначчи')
        n = int(input('>>>'))
    else:
        n = None
    glr = golden.count(a, b, extr_type, epsilon)
    fib = get_extremum_of_function_by_fibonacci_method(a, b, epsilon, n)
    return glr, fib
