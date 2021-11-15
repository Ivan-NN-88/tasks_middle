"""Что будет выведено в консоль в результате выполнения следующего кода?"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


print(B.__bases__[0].__subclasses__()[0])