import unittest
import LinkedList

class Linked_Test(unittest.TestCase):
    def test_linked_head_and_tail_node_is_always_set_at_none(self):
        link = LinkedList.Linked()
        self.assertIsNone(link.head, None)
        self.assertIsNone(link.tail, None)

    def test_linked_head_and_tail_node_is_can_change_while_head_is_added_twice(self):
        link = LinkedList.Linked()
        link.add_head('1st head')
        link.add_head('2nd head')
        self.assertIsNotNone(link.head)
        self.assertIsNotNone(link.tail)

if __name__ == '__main__':
    unittest.main()