'''Requiremnts: Understand how Linked lists works'''

'''A queue is a FIFO (First In First Out — the element placed at first can be accessed at first) structure 
which can be commonly found in many programming languages. 
This structure is named as “queue” because it resembles a real-world queue — people waiting in a queue.
'''
class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer


class Queue:
    '''A Queue is a Linked list that we can only remove or add a tail to'''
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return

        self.tail.pointer = Node(data, None)

        self.tail = self.tail.pointer

    def dequeue(self):
        if self.head is None:
            return None

        remove = self.head
        self.head = self.pointer

        if self.head is None:
            self.tail = None

            return "Empty Queue"
        return remove
