"""Укажите проблему в реализации дескриптора атрибутов."""


class Grade:
    def __init__(self):
        self._values = {}

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 1)

    def __set__(self, instance, value):
        if not (1 <= value <= 50):
            raise ValueError('Оценка должна быть от 1 до 5')
        self._values[instance] = value



# ========== ВАРИАНТЫ ОТВЕТА: ==========

# 1) Класс дескриптора должен быть явно унаследован от класса object.
# 2) Для хранения данных внутри дескриптора используется словарь, что будет приводить к утечкам памяти.
# 3) Отсутствует метод __delete__.
# 4) Данная реализация класса-дескриптора не содержит проблем.
# 5) Метод __set__ должен создавать исключение класса AttributeError.