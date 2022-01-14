from utils import *


def plot_hist_and_polygon(x, interval, title, distr, m=0, d=0, sigma=0):
    data_hist, k = create_hist(x, interval)
    data_polygon, k = create_polygon(x, interval)
    plot_hist(x, data_hist, k, interval, title, distr, m, d, sigma)
    plot_polygon(x, data_polygon, interval, title, distr, m, d, sigma)



def create_hist(X, interval):
    a = interval[0]
    b = interval[1]
    N = len(X)
    k = int(1 + 3.21 * math.log2(N))
    R = b - a
    width_interval = R / k
    data_hist = []
    for i in range(k):

        x_min = a + width_interval * i
        x_max = a + width_interval * (i + 1)
        count_elements = 0
        for x in X:
            if x_min < x <= x_max:
                count_elements += 1

            if x > x_max:
                break
        w = count_elements / (N * width_interval)
        data_hist.append([w, x_min, x_max])
    return data_hist, k


def create_polygon(X, interval):
    a = interval[0]
    b = interval[1]
    N = len(X)
    k = int(1 + math.log2(N))
    R = b - a
    width_interval = R / k
    data_polygon = []
    for i in range(k):
        q = a + width_interval * (i + 1)
        kq = 0
        for x in X:
            if x < q:
                kq += 1
        f = kq / N
        data_polygon.append([f, q])
    return data_polygon, k


def plot_hist(X, data_hist, k, interval, title, dstr, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    delta = (b - a) / k
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
    plt.title(title)
    plot_density_fn(X, a, b, dstr, m, d, sigma)
    plt.show()


def plot_polygon(X, data_polygon, interval, title, dstr, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    x = [a]
    y = [0]
    for i in data_polygon:
        y.append(i[0])
        x.append(i[1])
        plt.scatter(x, y)
    plt.step(x, y)
    plt.title(title)

    plot_density_f(X, a, b, dstr, m, d, sigma)
    plt.show()

