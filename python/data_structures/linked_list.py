class Node:
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        stringval = self.head
        string_values = ""
        while stringval is not None:
            string_values += f"{ {stringval.value} } -> "
            stringval = stringval.next
        string_values += "NULL"
        return string_values

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    class TargetError:
        pass