from config import Config


class GoldenRatio:
    r_golden = 2 / (1 + 5 ** 0.5)
    a, b, xl, xr = 0, 0, 0, 0

    def delete_left(self):
        self.a = self.xl
        self.xl = self.xr
        self.xr = self.a + (self.b - self.a) * self.r_golden

    def delete_right(self):
        self.b = self.xr
        self.xr = self.xl
        self.xl = self.b - (self.b - self.a) * self.r_golden

    def count(self, a, b, extr_type, epsilon: float) -> tuple:
        iterations = 0
        self.a, self.b, func = a, b, Config.our_function
        interval = b - a
        self.xl = b - interval * self.r_golden
        self.xr = a + interval * self.r_golden

        while (self.b - self.a) >= epsilon:
            iterations += 1
            if extr_type == 1:
                if func(self.xl) > func(self.xr):
                    self.delete_right()
                    continue
                self.delete_left()
            if extr_type == 2:
                if func(self.xl) < func(self.xr):
                    self.delete_left()
                    continue
                self.delete_right()

        x = (self.b + self.a) / 2
        return round(x, 3), round(func(x), 3), f'Число итераций: {iterations}'
