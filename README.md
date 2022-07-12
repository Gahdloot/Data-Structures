#Data Structure:


Data Structures are a specialized means of organizing and storing data in computers in such a way that we can perform operations on the stored data more efficiently. Data structures have a wide and diverse scope of usage across the fields of Computer Science and Software Engineering.

Data structures are being used in almost every program or software system that has been developed. Moreover, data structures come under the fundamentals of Computer Science and Software Engineering. It is a key topic when it comes to Software Engineering interview questions. Hence as developers, we must have good knowledge about data structures.

In this project, I will be briefly explain commonly used data structures every programmer must know.

##Linked list
linked list is a sequential structure that consists of a sequence of items in linear order which are linked to each other. Hence, you have to access data sequentially and random access is not possible. Linked lists provide a simple and flexible representation of dynamic sets.

Let’s consider the following terms regarding linked lists.

    -Elements in a linked list are known as nodes.
    
    -Each node contains a key and a pointer to its successor node, known as next.
    
    -The attribute named head points to the first element of the linked list.
    
    -The last element of the linked list is known as the tail.

##Stacks
A stack is a LIFO (Last In First Out — the element placed at last can be accessed at first) structure which can be commonly found in many programming languages. This structure is named as “stack” because it resembles a real-world stack — a stack of plates.

Stack operations
Given below are the 2 basic operations that can be performed on a stack.

    -Push: Insert an element on to the top of the stack.
    
    -Pop: Delete the topmost element and return it.


##Queues
A queue is a FIFO (First In First Out — the element placed at first can be accessed at first) structure which can be commonly found in many programming languages. This structure is named as “queue” because it resembles a real-world queue — people waiting in a queue.

##Hash Tables
A Hash Table is a data structure that stores values which have keys associated with each of them. Furthermore, it supports lookup efficiently if we know the key associated with the value. Hence it is very efficient in inserting and searching, irrespective of the size of the data.

Direct Addressing uses the one-to-one mapping between the values and keys when storing in a table. However, there is a problem with this approach when there is a large number of key-value pairs. The table will be huge with so many records and may be impractical or even impossible to be stored, given the memory available on a typical computer. To avoid this issue we use hash tables.

###Hash Function
A special function named as the hash function (h) is used to overcome the aforementioned problem in direct addressing.

In direct accessing, a value with key k is stored in the slot k. Using the hash function, we calculate the index of the table (slot) to which each value goes. The value calculated using the hash function for a given key is called the hash value which indicates the index of the table to which the value is mapped.

**h(k) = k % m**

    -h: Hash function
    
    -k: Key of which the hash value should be determined
    
    -m: Size of the hash table (number of slots available). A prime value that is not close to an exact power of 2 is a good choice for m.

