class Node(object):
    def __init__(self, data, nextt):
        self.__data = data
        self.__next = nextt
        self.__index = 0

    def index_list(self):
        if self.__next is None:
            return
        self.__next.set_index(self.__index+1)
        self.__next.index_list()

    def get_index(self):
        return self.__index

    def set_index(self, newindex):
        self.__index = newindex

    def replace_at_index(self, index, data):
        if self.__next is None:
            return print("Nie znaleziono tego indeksa.")
        elif str(self.__index) == str(index):
            self.__data = data
            self.index_list()
            return
        self.__next.replace_at_index(index, data)

    def add_at_index(self, index, data):
        if self.__next is None:
            return print("Nie znaleziono tego indeksa.")
        elif str(self.__index) == str(index):
            self.__next = Node(data, self.__next)
            return
        self.__next.add_at_index()

    def add_to_end(self, newhead):
        if self.__next is None:
            self.__next = Node(newhead, None)
            self.index_list()
            return
        self.__next.add_to_end(newhead)

    def delete_from_end(self):
        if self.__next.__next is None:
            self.__next = None
            return
        self.__next.delete_from_end()

    def print_list(self):
        print("Index: " + str(self.__index) + ", Data: " + str(self.__data))
        if self.__next is None:
            return
        self.__next.print_list()

    def get_next(self):
        return self.__next

    def set_next(self, newnext):
        self.__next = newnext
