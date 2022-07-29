
'''A linked list is a system that links object together by
tracing location of the next object from the current object'''


'''linked list is a sequential structure that consists of a sequence of items in 
a linear order which are linked to each other. 
Hence, you have to access data sequentially and random access is not possible. 
Linked lists provide a simple and flexible representation of dynamic sets.

Let’s consider the following terms regarding linked lists.

    -Elements in a linked list are known as nodes.
    
    -Each node contains a key and a pointer to its successor node, known as next.
    
    -The attribute named head points to the first element of the linked list.
    
    -The last element of the linked list is known as the tail.'''

class Node:
    '''When a node is created, it holds two attributes,
    1. The Data: which is the data of the attribute
    2. Pointer(next node): Which is the location to the Next Node'''
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class Linked:
    '''This is a Linked list class'''
    def __init__(self):
        '''if data can be linked, then there has to be a beginning(Head) and an ending(tail)'''
        self.head = None
        self.tail = None
        '''We first have to set the Linked is to Head and tail to None since when Linked list is first
        instantiated, it has no Node in it to trace any Location'''



    def add_head(self, data):
        '''To start a linked list, you first have to set an head, which is basically just a node
        and if there are no other nodes, the head also becomes the tail'''
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head


        else:
            '''if there is a preexisting head,
             the new node becomes the while the previous head now becomes the pointer'''
            New_node = Node(data, self.head)

            self.head = New_node


    def add_tail(self, data):
        '''If there is no head on the linked list, the new node become the head and the tail '''
        if self.head is None:
            self.add_head(data)

        elif self.tail.pointer is None:
            '''If there is an Existing tail, the old tail becomes a pointer for the new tail'''
            new_tail = Node(data)
            self.tail.pointer = new_tail
            self.tail = new_tail


        else:
            print('something is wrong with adding a tail')

    def remove_head(self):
        self.head = self.head.pointer

    def remove(self, search):
        '''Removing to remove a Node in a linked list,
        you have to keep track of both the previous node and the next node
        so as to reassing the pointer of the previous node ot the next node'''
        if self.head is None:
            return None

        node = self.head
        while node:
            if search is node.data and node is self.head:
                self.remove_head()
                break
            elif search is node.pointer.data:
                node.pointer = node.pointer.pointer
                break
            else:
                node = node.pointer




    def search(self, user_id):
        node = self.head

        while node:
            if node.data is user_id:
                return node.data
            else:
                node = node.pointer
        return None




    def print_string(self):
        chain = 'node chain ****:'
        node = self.head
        if node is None:
            print('None node added')

        while node:
            chain += f'{node.data} ->'
            node = node.pointer
        chain += ' None'
        print(chain)

    def to_list(self):
        '''Looping through all the node and inserting the into a list(array)'''
        list_of_linked_data = []
        if self.head is None:
            return list_of_linked_data
        else:
            node = self.head
            while node:
                list_of_linked_data.append(node.data)
                node = node.pointer
            return list_of_linked_data

    def lenght_of_list(self):
        return len(self.to_list())


'''Example:'''


'''ll = Linked()

ll.add_tail('Ending Ender')
ll.add_head('The head')
ll.add_tail('Tail 1')
ll.add_tail('Tail 2')
ll.add_tail('Tail 3')
ll.add_tail('Tail 4')
ll.add_tail('Tail 5')

print(ll.search('Tail 4'))
ll.remove_head()

ll.print_string()

ll.remove('Ending Ender')
ll.print_string()
#ll.print_string()
'''