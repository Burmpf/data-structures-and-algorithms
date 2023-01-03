from data_structures.invalid_operation_error import InvalidOperationError


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        # if self.top is None:
        #     self.top = Node(value)
        #     return
        # old = self.top
        self.top = Node(value, self.top)
        #self.top.next = old

    def pop(self):
        try:
            val = self.top
            self.top = self.top.next
            return val.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.top.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top:
            return False
        else:
            return True




class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    #both start empty
    
    def enqueue(self, value):
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        self.stack1.push(value)

    def dequeue(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()