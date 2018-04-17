"""
O primeiro elemento que entrou é o primeiro a sair.
A inserção ocorre no final.
FIFO - first in first out
"""


class Queue:

    def __init__(self):
        self.fila = []
        self.len_fila = 0

    def push(self, e):
        self.fila.append(e)
        self.len_fila += 1

    def pop(self):
        if not self.empty():
            self.fila.pop(0)
            self.len_fila -= 1


    def empty(self):
        if self.len_fila == 0:
            return True
        return False

    def length(self):
        return self.len_fila

    def top(self):
        if not self.empty():
            return self.fila[0]
