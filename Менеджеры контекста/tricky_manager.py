"""Укажите, что будет выведено в консоль в результате работы кода:"""


class TrickyManager:
    def __init__(self, lst):
        self.worklist = lst

    def __enter__(self):
        __builtins__.print = lambda x, f=open('trace.log', 'a'), end='\n': f.write(str(x))
        return 'T-R-I-C-K-Y'

    def __exit__(self, exc_type, exc_val, trace):
        return True


with TrickyManager([1, 2, 3, 4, 5]) as t:
    for c in t:
        print(c, end=' ')

print(t)