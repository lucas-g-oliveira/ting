from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.itens = []
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.itens.append(value)

    def dequeue(self):
        if self.length > 0:
            temp = self.itens[0]
            self.itens = self.itens[1:]
            self.length -= 1
            return temp
        return None

    def search(self, index):
        if index > self.length:
            raise IndexError("Índice Inválido ou Inexistente")

        return self.itens[index]
