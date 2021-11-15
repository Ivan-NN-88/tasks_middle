"""Чему будет равно значение переменной global_resource в результате выполнения следующего кода?"""

from threading import Thread, Lock


COUNT = 1000000
resource_lock = Lock()
global_resource = 0


def producer():
    global global_resource
    for i in range(COUNT):
        global_resource += 1


def consumer():
    global global_resource
    for i in range(COUNT):
        global_resource -= 1


if __name__ == "__main__":
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)
    t1.start()
    t2.start()

    print(global_resource)



# ===========================ВАРИАНТЫ ОТВЕТА=====================================

"""
    1) -100000
    2) 100000
    3) Значение не может быть строго определено, так как глобальная переменная изменяется в двух потоках без блокировок.
    4) Значение не может быть строго определено, так как не выполняется присоединение к потокам методом .join().
    5) Значение не может быть строго определено, так как неизвестен момент завершения потоков - дочерние потоки 
    завершатся вместе с основным потоком.
    6) 0
"""

