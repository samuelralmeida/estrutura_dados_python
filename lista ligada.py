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
                        current_index += 1

            self.len_list += 1

    def pop(self, index):

        if not self.empty() and 0 <= index < self.len_list:

            flag_remove = False

            if self.first.get_next() is None:
                # Possui apenas um elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do inicio, mas possui mais de 1  elemento
                self.first = self.first.get_next()
                flag_remove = True
            else:
                # Se chegou aqui a lista possui mais de um elemento e a remoção não é no inicio
                prev_node = self.first
                curr_node = self.first.get_next()
                curr_index = 1

                while curr_node is not None:

                    if index == curr_index:
                        # o proximo do anterios tem que apontar para o ŕóximo do nó corrente
                        prev_node.set_next(curr_node.get_next())
                        curr_node.set_next(None)
                        flag_remove = True
                        break

                    prev_node = curr_node
                    curr_node = curr_node.get_next()
                    curr_index += 1

            if flag_remove:
                self.len_list -= 1

    def empty(self):
        if self.first is None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):

        curr_node = self.first

        while curr_node is not None:
            print(curr_node.get_label(), end=' ')
            curr_node = curr_node.get_next()
        print('')


lista = LinkedList()

lista.push('samu', 0)
lista.show()
lista.push('rod', 1)
lista.show()
lista.push('alme', 0)
lista.show()
lista.push('sou', 2)
lista.show()

lista.pop(0)
lista.show()
lista.pop(2)
lista.show()
