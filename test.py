import unittest
import LinkedList

class Linked_Test(unittest.TestCase):
    def test_linked_head_node_is_always_set_at_none(self):
        link = LinkedList.Linked()
        self.assertIsNone(link.head, None)
        self.assertIsNone(link.tail, None)

if __name__ == '__main__':
    unittest.main()