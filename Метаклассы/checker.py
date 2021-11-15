"""Укажите позицию в коде, когда будет срабатывать функционал метакласса Checker:"""


class Checker(type):
    def __new__(cls, name, bases, cls_dict):
        return super().__new__(cls, name, bases, cls_dict)


class Experiment(metaclass=Checker):    # 1
    counter = 0
                                        # 2
    def __init__(self):
        self.state = 0                  # 3

    def start(self):
        self.state = 1
                                        # 4

exp = Experiment()                      # 5
exp.start()                             # 6