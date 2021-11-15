"""Какое значение будет храниться в переменной x в результате работы следующего кода?"""


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


x = None
avg = make_averager()
for i in range(4):
    x = avg(i)

print(x)
