"""Укажите последовательность вызова методов класса Stranger в следующем коде: """


class Stranger:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __mul__(self, n=5):
        return str(self) * n

    @staticmethod
    def z(self, n=7):
        return self * n


s = Stranger(3)
print(s.z(9))
