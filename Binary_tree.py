'''A Binary tree consist of intergers which are arranged according to their size'''



class Node:
    '''Unlike a Linked list, The Node in a Binary tree has Three(3) attributes
    1. The data: which should have an interger in it
    2. The left: Which consist of Numbers that are less than the data
    3. The Right: Which consist of Numbers that are greater than the data'''
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        '''Every Binary tree starts with a root-Node(Which is like a head) from which other node flow through'''
        self.root = None

    def _insert_recursive(self, value, node):
        '''A recursive Function to move through the Binary tree'''
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node()

    def insert(self, value):
        '''A Method to Move to the Binary Tree'''
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _search_recursive(self, value, node):

        if value == node.data:
            return node.data

        if value < node.data and node.left is not None:
            if value == node.left.data:
                return node.left.data
            return self._search_recursive(value, node.left)
        elif value > node.data and node.right is not None:
            if value == node.right.data:
                return node.right.data
            return self._search_recursive(value, node.right)

        return None


    def search(self, value):
        value = int(value)
        if self.root is None:
            return False
        return self._search_recursive(value, self.root)
