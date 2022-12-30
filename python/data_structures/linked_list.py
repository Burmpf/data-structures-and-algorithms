class Node:
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.count = 0

    def __str__(self):
        current = self.head
        string_values = ""
        while current is not None:
            string_values += f"{{ {str(current.value)} }} -> "
            current = current.next
        string_values += "NULL"
        return string_values

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def insert_before(self, before, value):
        current = self.head
        previous = None
        try:
            while current.value is not before:
                previous = current
                current = current.next
            new_node = Node(value)
            new_node.next = current
            if previous is not None:
                previous.next = new_node
            if previous is None:
                self.head = new_node
        except Exception as e:
            raise TargetError(e)

    def insert_after(self, after, value):
        current = self.head
        try:
            while current.value is not after:
                current = current.next
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
        except Exception as e:
            raise TargetError(e)

    def kth_from_end(self, value):
        current = self.head
        length = 0
        while current is not None:
            current = current.next
            length += 1
        if value >= length:
            raise TargetError(Exception)
        if value < 0:
            raise TargetError(Exception)
        current = self.head
        for x in range(0, length-value - 1):
            print(current.value)
            current = current.next
        return current.value


class TargetError(Exception):
    print("searching for value that doesnt exist")
    pass