from python.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval


class Queue:
    """
    Linked list that functions as a Queue. Knows its head and tail, enqueue adds to tail and dequeue removes from head
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        string = "blank"
        while current:
            string += current.value.value + "->"
            current = current.next
        return string

    # def enqueue(self, value):
    #     if self.tail:
    #         self.tail.next = Node(value)
    #         self.tail = self.tail.next
    #         return
    #     else:
    #         self.tail = self.head = Node(value)
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node

    def dequeue(self):
        # consider a queue with only 1 node
        # TODO: refactor class to include a .length
        try:
            if self.head == self.tail:
                dequeued = self.head
                self.head = self.tail = None
                return dequeued.value

            dequeued = self.head
            self.head = self.head.next
            return dequeued.value

        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    # def dequeue(self):
    #     try:
    #         dequeued = self.head
    #         self.head = self.head.next
    #         return dequeued.value
    #     except Exception as e:
    #         raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.head.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.head is None