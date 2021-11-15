"""
Укажите корректный способ обращения к сопрограммам df и pp в коде ниже, чтобы в
консоль выдались целочисленные данные из строки data (1147 и -4):
"""


def producer(data, next_task):
    tokens = data.split(";")
    for token in tokens:
        next_task.send(token)
    next_task.close()


def df(tf=int, next_task=None):
    try:
        while True:
            token = (yield)
            try:
                token = tf(token)
            except:
                pass
            else:
                next_task.send(token)
    except GeneratorExit:
        pass


def pp():
    try:
        while True:
            token = (yield)
            print('->', token)
    except GeneratorExit:
        pass


data = "Moscow;1147;-4"
