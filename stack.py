class Stack:

    def __init__(self, some_list: list):
        self.some_list = some_list

    def is_empty(self):
        if len(self.some_list) == 0:
            return True
        else:
            return False

    def push(self, element):
        return self.some_list.insert(0, element)

    def pop(self):
        return self.some_list.pop(0)

    def peek(self):
        return self.some_list[0]

    def size(self):
        return len(self.some_list)
