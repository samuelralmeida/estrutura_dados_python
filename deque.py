"""
Deque: double-ended queue - fila de duas pontas
Você pode inserir ou remover nas duas pontas
"""


class Deque:

    def __init__(self):
        self.len = 0
        self.deque = []

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.append(e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len += 1

    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -= 1

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]

    def show(self):
        for i in self.deque:
            print(i, end=' ')
