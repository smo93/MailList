import unittest
import mail
from maillist import MailList


class MailTest(unittest.TestCase):
    """docstring for MailTest"""
    def setUp(self):
        self.lists = {1: MailList('list1'), 2: MailList('list2')}

    def test_show_lists(self):
        expected = '[1] - list1\n[2] - list2\n'
        self.assertEqual(expected, mail.show_lists(self.lists))

    def test_show_list(self):
        self.lists[1].add_user('ivan', 'dragan@petkan')
        self.assertEqual('[1] ivan - dragan@petkan', mail.show_list(self.lists, 1))

    def test_show_list_with_bad_id(self):
        self.assertFalse(mail.show_list(self.lists, 3))

    def test_create_list(self):
        lists = {}
        mail.create_list(lists, 'list1')
        self.assertEqual('[1] - list1\n', mail.show_lists(lists))

    def test_add_new_user(self):
        result = mail.add_new_user(self.lists, 1, 'ivan', 'dragan@petkan')
        self.assertTrue(result)
        self.assertEqual('[1] ivan - dragan@petkan',\
                mail.show_list(self.lists, 1))

    def test_add_new_user_in_non_existent_list(self):
        self.assertFalse(mail.add_new_user(self.lists, 4, 'a', 'b'))
        

if __name__ == '__main__':
    unittest.main()

