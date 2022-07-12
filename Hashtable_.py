'''Requiremnts: Understand how Linked lists works'''

'''A Hash Table is a data structure that stores values which have keys associated with each of them. 
Furthermore, it supports lookup efficiently if we know the key associated with the value. 
Hence it is very efficient in inserting and searching, irrespective of the size of the data.

Direct Addressing uses the one-to-one mapping between the values and keys when storing in a table. 
However, there is a problem with this approach when there is a large number of key-value pairs. 
The table will be huge with so many records and may be impractical or even impossible to be stored, 
given the memory available on a typical computer. 
To avoid this issue we use hash tables.
'''

class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class Data:
    '''A Hash table consists of keys and values just like a dictionary'''
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    '''When an hash table in instantiated,
    it is supposed to have a table size which stands for lenght of rows that can be inserted into the hashtable.
    the columns of an hashtable are
    1. Key (which will be hashed)
    2. Value
    '''
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def get_hash(self, key):
        '''hashing a key means converting the key into an interger
         which must not be more than the table-size(lenght) of the rows in the hash table.
         So, if an hash table has a table-size(lenght) of 15, no key must have a value of 15 or above,
         hash table couting starts from Zero(0)'''
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            #trail
        hash_value = hash_value % self.table_size
        return hash_value

    def add_kv(self, key, value):
        '''To add a data to the hashtable, we first have to hash the key'''
        hashed_key = self.get_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            '''If the key Exist, which could mean 2 things
            1. Our hash table has more keys than the required amount of table-size(lenght)
            2. Our hashing method produced the same hash for two or more key
            It is called Collision.
            The most Efficient thing to do is to create a linked list within the hash value'''
            node = self.hash_table[hashed_key]
            while node.pointer:
                node = node.pointer
            node.pointer = Node(Data(key, value), None)

    def get_value(self, key):
        '''To get the value from an hashtale,
        we have to hash the key again and find for a similar hash in the hashtable'''
        hashed_key = self.get_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.pointer is None:
                return node.data.value
            while node.pointer:
                if key == node.data.key:
                    return node.data.value
                node = node.pointer

            if key == node.data.key:
                return node.data.value

        return None


