from python.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval

        
class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.rear = None

    def enqueue(self,value):
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    
    def dequeue(self):
        try:
            dequeued = self.head
            self.head = self.head.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.head.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.head is None