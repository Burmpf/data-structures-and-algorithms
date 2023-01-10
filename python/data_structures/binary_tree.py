class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, root=None, nodes=None):
        try:
            if root is None:
                root = self.root
            if nodes is None:
                nodes = []
            nodes.append(root.value)
            if root.left:
                self.pre_order(root.left, nodes)
            if root.right:
                self.pre_order(root.right, nodes)
            return nodes
        except:
            return None

    def in_order(self, root=None, nodes=None):
        try:
            if root is None:
                root = self.root
            if nodes is None:
                nodes = []
            if root.left:
                self.in_order(root.left, nodes)
            nodes.append(root.value)
            if root.right:
                self.in_order(root.right, nodes)
            return nodes
        except:
            return None

    def post_order(self, root=None, nodes=None):
        try:
            if root is None:
                root = self.root
            if nodes is None:
                nodes = []
            if root.left:
                self.post_order(root.left, nodes)
            if root.right:
                self.post_order(root.right, nodes)
            nodes.append(root.value)
            return nodes
        except:
            return None

    def find_maximum_value(self):
        if self.root is None:
            return None
        return max(self.post_order())

