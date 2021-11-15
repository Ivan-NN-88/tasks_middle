"""Укажите результат выполнения следующего кода: """


class Slack:
    def __init__(self):
        self.foo = -1

    def __getattr__(self, name):
        setattr(self, name, 1)
        return 11

    def __getattribute__(self, name):
        return super().__getattribute__(name) + 1

    def __setattr__(self, name, value=0):
        super().__setattr__(name, value)


data = Slack()
data.foo += 1
print(data.foo)
