"""Что будет выведено в консоль в результате работы следующего кода?"""

x = 13


class C:
    x = 2
    print(x)

    def m(self):
        C.x = 4
        print(x)


i = C()
i.m()
print(x)
