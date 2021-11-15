"""Укажите, что будет выведено в консоль в результате выполнения кода?"""


class Base:
    var = 5
    def __init__(self):
        pass


class X(Base):
    def __init__(self):
        super().__init__()
        self.var = 7


class Y(Base):
    var = 10
    def __init__(self):
        super().__init__()


class Z(X, Y):
    def __init__(self):
        self.var = 13


z = Z()
print(super(Z, z).var)