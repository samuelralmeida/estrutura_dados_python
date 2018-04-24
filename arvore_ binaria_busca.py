"""
Dado um nó, todos os elementos a esquerda possuem chave menor; os que estão à direita do nó possuem chave maior
"""

class Node:

    def __init__(self, label):
        self.label = label
        # apontador para filhos da direita e esquerda
        self.left = None
        self.right = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):

        # cria nó
        node = Node(label)

        # verifica se a árvore está vazia
        if self.empty():
            self.root = node
        else:
            # árvore não vazia, insere recursivamente
            dad_node = None
            curr_node = self.root

            while True:

                if curr_node != None:
                    dad_node = curr_node

                    # verifica se vai para esquerda ou direita
                    if node.getLabel() < curr_node.getLabel():
                        # vai para esquerda
                        curr_node = curr_node.getLeft()
                    else:
                        # vai para direita
                        curr_node = curr_node.getRight()

                else:

                    # se curr_node É none, é onde inserir
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)

                    break

    def empty(self):
        if self.root == None:
            return True
        return False

    # mostra em pré-ordem (raiz-esquerda-direita)
    def show(self, curr_node):

        if curr_node != None:
            print('{}'.format(curr_node.getLabel()), end=' ')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())

    def getRoot(self):
        return self.root

    def remove(self, label):
        """
        CASO 1 - nó removido não tem filho (chamado de folha também), o nó é retirado
        CASO 2 - nó removido tem apenas 1 filho, esse filho ocupa o lugar do nó removido
        CASO 3 - nó removido com 2 filhos, pega o menor elemento da subarvore a direita e substitui o removido
        """

        dad_node = None
        curr_node = self.root

        while curr_node != None:

            # verifica se encontrou o nó a ser removido
            if label == curr_node.getLabel():

                # caso 1
                if curr_node.getLeft() == None and curr_node.getRight() == None:

                    # verifica se é a raiz
                    if dad_node == None:
                        self.root = None
                    else:
                        # verifica se é filho a esquerda ou direita
                        if dad_node.getLeft() == curr_node:
                            # filho a esquerda
                            dad_node.setLeft(None)
                        elif dad_node.getRight() == curr_node:
                            # filho a direita
                            dad_node.setRigth(None)

                # caso 2
                elif (curr_node.getLeft() is None and curr_node.getRight() is not None) or \
                     (curr_node.getLeft() is not None and curr_node.getRight() is None):

                    # verifica se o nó a ser removido é raiz
                    if dad_node == None:
                        # verifica se o filho de curr_node é filho a esquerda
                        if curr_node.getLeft() != None:
                            self.root = curr_node.getLeft()
                        else:
                            # filho é a direita
                            self.root = curr_node.getRight()
                    # se não for raiz
                    else:
                        # verifica se o filho de curr_node é filho à esquerda
                        if curr_node.getLeft() != None:
                            # verifica se curr_node é filho a esquerda
                            if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                                dad_node.setLeft(curr_node.getLeft())
                            else:
                                # curr_node é filho a direita
                                dad_node.setRight(curr_node.getLeft())
                        else:
                            # filho de curr_node é filho à esquerda
                            # verifica se curr_node é filho a esquerda
                            if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                                dad_node.setLeft(curr_node.getRight())
                            else:
                                # curr_node é filho a direita
                                dad_node.setRight(curr_node.Right())

                # caso 3






t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.show(t.getRoot())
