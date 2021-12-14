import numpy as np
import matplotlib.pyplot as plt


def gorner_approx(x, y, power, label):
    fp, residuals, rank, sv, rcond = np.polyfit(x, y, power, full=True)
    fp = list(fp)
    x_values = np.linspace(np.min(x), np.max(x), 1000)
    y_values = []
    for value in x_values:
        S = fp[0]
        for i in range(len(fp) - 1):
            S = S * value + fp[i + 1]
        y_values.append(S)
    plt.plot(x_values, y_values)
    print(f"Суммарная ошибка отклонения для графика {label}:")
    print(residuals)



def polynomial_approx(x, y, power, label):
    fp, residuals, rank, sv, rcond = np.polyfit(x, y, power, full=True)
    polynom = fp
    polynom_function = np.poly1d(polynom)
    x_values = np.linspace(np.min(x), np.max(x), 1000)
    y_values = polynom_function(x_values)
    plt.plot(x_values, y_values)
    print(f"Суммарная ошибка отклонения для графика {label}:")
    print(residuals)


