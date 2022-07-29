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

    def test_linked_list_can_be_converted_to_list(self):
        link = LinkedList.Linked()
        link.add_head('1st head')
        link.add_head('2nd head')
        link.add_head('3rd head')
        link.add_head('4th head')
        lenght_of_list = link.lenght_of_list()
        self.assertEqual(lenght_of_list, 4)

    def test_that_removeMethod_works(self):
        link = LinkedList.Linked()
        link.add_head('1st head')
        link.add_head('2nd head')
        link.add_head('3rd head')
        link.add_head('4th head')
        link.remove('2nd head')
        lenght_of_list = link.lenght_of_list()
        self.assertEqual(lenght_of_list, 3)


if __name__ == '__main__':
    unittest.main()