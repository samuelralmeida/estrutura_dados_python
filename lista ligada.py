"""
Também chamada de lista encadeada
Essa lista é compost por nós ou vertices, cada nó armazena uma entidade.
Essa entidade pode ser string, int, lista,, objeto, etc.
Cada nó guarda referência para o próximo nó, por isso lista ligada
"""


class Node:

    def __init__(self, label):
        self.label = label
        self.next = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):
        if index >= 0:
            node = Node(label)

            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    # Inserção no inicio
                    node.set_next(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # Inserção no final
                    self.last.set_next(node)
                    self.last = node
                else:
                    # Inserção no meio
                    prev_node = self.first
                    current_node = self.first.get_next()
                    current_index = 1

                    while current_node is not None:

                        if current_index == index:
                            # Set o current_node como o próximo do nó
                            node.set_next(current_node)
                            # Set o node como próximo do prev_node
                            prev_node.set_next(node)
                            break

                        prev_node = current_node
                        current_node = current_node.get_next()
                        current_node += 1

            self.len_list += 1
