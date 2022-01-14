

class Config:
    interval_start = -3
    interval_end = 3

    @staticmethod
    def our_function(x):
        return x * (x * ((1/3) * x - 1) - 3)


