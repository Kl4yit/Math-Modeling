def interval_text():
    a = float(input("Введите начальное значение интервала: "))
    b = float(input("Введите конечное значение интервала: "))
    return a, b


def gauss_text():
    m_gauss = float(input("Введите мат ожидание для распределения Гаусса: "))
    d_gauss = float(input("Введите дисперсию для распределения Гаусса: "))
    return m_gauss, d_gauss


def reley_text():
    s_reley = float(input("Введите сигму для релеевского закона: "))
    b = float(input("Введите правую границу интервала [a, b]: "))
    return s_reley, b

