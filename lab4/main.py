from numerals import find_numerals
from plotter import plot_hist_and_polygon
from gaussian import gaussian_sampling
from reversed import reversed_functions
from reley import reley_sampling
from text import interval_text

def main():
    print("1 - Выборка непрерывных равно распределенных случайных величин методом обратных функций")
    print("2 - Выборка величин, распредленных по Гауссовскому закону с математическим ожиданием и дисперсией")
    print("3 - Выборка случайных значенй по методу Неймана")

    option = input(">>>")

    if (option == '1'):
        a, b = interval_text()
        x, interval = reversed_functions(a, b)
        distr, title = 1, "Равномерное распределение"
        plot_hist_and_polygon(x, interval, title, distr)
        find_numerals(x, 0, distr)
    if (option == '2'):
        x, interval, m, d = gaussian_sampling()
        distr, title = 2, "Распределение Гаусса"
        plot_hist_and_polygon(x, interval, title, distr, m, d)
        find_numerals(x)
    if (option == '3'):
        x, interval, sigma = reley_sampling()
        distr, title = 3, "Распределение Релея"
        plot_hist_and_polygon(x, interval, title, distr, 0, 0, sigma)
        find_numerals(x, sigma, distr)




if __name__ == "__main__":
    main()
