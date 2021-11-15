"""Что будет выведено в консоль в результате работы кода?"""


def make_multiplier_of(n):
    lst = []
    def multiplier(x, final=False):
        lst.append(x * n)
        if final:
            print(lst)
        return x * n
    return multiplier


times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

times3(9)
times5(3)
times5(times3(2), True)