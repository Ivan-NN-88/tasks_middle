"""Укажите верное продолжение утверждения: “В строке `foo.zzz = 77` ошибка не возникает, потому что…”"""


class Base:
    __slots__ = ('y', 'z')


class Child(Base):
    name = 'Figaro'
    num = 99


foo = Child()
foo.zzz = 77
print(foo.zzz)



# ===========================ВАРИАНТЫ ОТВЕТА=====================================

# 1) нет правильного ответа.
# 2) ошибка произойдёт раньше - дочерний класс не может содержать атрибуты, которых нет в __slots__ родительского класса.
# 3) дочерний класс имеет атрибуты, отличные от тех, которые описаны в __slots__ - для них создаётся атрибут __dict__,
# куда в дальнейшем заносятся все "неизвестные" атрибуты.
# 4) дочерний класс не наследует атрибут __slots__, все новые атрибуты добавляются в стандартный __dict__.
# 5) дочерний класс наследует атрибут __slots__, но имеет также и атрибут __dict__, куда добавляются новые атрибуты.
# 6) все "неизвестные" атрибуты всегда добавляются в атрибут __dict__ объекта - это обычное поведение Python-объектов.