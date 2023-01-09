from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            input_node, current = Node(value), self.root
            while value != current.value:
                if value < current.value:
                    if current.left is None:
                        current.left = input_node
                        break
                    current = current.left
                if value > current.value:
                    if current.right is None:
                        current.right = input_node
                        break
                    current = current.right

    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            if value > current.value:
                current = current.right
        return False