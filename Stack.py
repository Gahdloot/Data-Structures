'''Requiremnts: Understand how Linked lists works'''

'''A stack is a LIFO (Last In First Out — the element placed at last can be accessed at first) structure 
which can be commonly found in many programming languages. 
This structure is named as “stack” because it resembles a real-world stack — a stack of plates.
'''

class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer


class Stack:
    '''A Queue is a Linked list that we can only remove or add a Head to'''
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top

    def push(self, data):
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        if self.top is None:
            return None
        else:
            removed = self.top
            new_top = self.top.pointer
            self.top = new_top
            return removed