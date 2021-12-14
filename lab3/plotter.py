import matplotlib.pyplot as plt
from parser import parse_json_data
from approximation import *
from text_interface import solve_method

class Plotter:

    def __init__(self, function) -> None:
        self.function = function

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.data = parse_json_data(call)
        self.plot_approximation(self.data)
        return self.data

    def _plot(self, x, y, label):
        plt.scatter(x, y, label=label)

    def _setting_and_show(self, title):
        plt.xlabel("Значение по X")
        plt.ylabel("Значение по Y")
        plt.title(title)
        plt.legend()
        plt.show()

    def plot_approximation(self, data):
        power = int(input("Степень аппроксимирующего полинома: "))
        solve_method()
        option = int(input('>>> '))

        for label, cords in data.items():
            if option == 1:
                polynomial_approx(cords['x'], cords['y'], power, label)
            else:
                gorner_approx(cords['x'], cords['y'], power, label)
            plt.scatter(cords['x'], cords['y'], label=label)
        self._setting_and_show("Задача аппроксимации")
