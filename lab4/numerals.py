from utils import *



def find_numerals(x, sigma = 0, distr = 0):
    sigma_rayleigh = sigma
    if distr == 1:
        m_n = (min(x) + max(x)) / 2
    if distr == 3:
        m_n = math.sqrt(math.pi / 2) * sigma_rayleigh
    m = find_mathematical_expectation(x)
    print("Первый выборочный момент(выборочное среднее):", round(m, 4))
    print("Второй выборочный момент(дисперсия) c неизвестным МО:", round(find_dispersion(x, m), 4))
    print("Второй выборочный момент(дисперсия) c известным МО:", round(find_dispersion(x, m_n), 4))
