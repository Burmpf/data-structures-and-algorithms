from python.data_structures.invalid_operation_error import InvalidOperationError

class Node: 

    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            return
        old = self.top
        self.top = Node(value)
        self.top.next = old

    def pop(self):
        try:
            value = self.head.value
            self.head = self.head.next
            return value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.head.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.head is None
