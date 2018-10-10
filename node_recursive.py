class Node(object):
    def __init__(self, data, nextt):
        self.__data = data
        self.__next = nextt

    def add_to_end(self, newhead):
        if self.__next is None:
            self.__next = Node(newhead, None)
            return
        self.__next.add_to_end(newhead)

    def print_list(self):
        print(self.__data)
        if self.__next is None:
            return
        self.__next.print_list()


    def get_next(self):
        return self.__next

    def set_next(self, newnext):
        self.__next = newnext
