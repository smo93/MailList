import unittest
import mail
from maillist import MailList


class MailTest(unittest.TestCase):
    """docstring for MailTest"""
    def setUp(self):
        self.lists = {1: MailList('list1'), 2: MailList('list2')}

    def test_merge_empty_lists(self):
        mail.merge(self.lists, 1, 2, 'list3')
        expected = '[1] - list1\n[2] - list2\n[3] - list3\n'
        self.assertEqual(expected, mail.show_lists(self.lists))

    def test_merge_non_empty_lists(self):
        mail.add_new_user(self.lists, 1, 'asd', 'asd')
        mail.add_new_user(self.lists, 2, 'dsa', 'dsa')
        mail.merge(self.lists, 1, 2, 'list3')
        expected = '[1] asd - asd\n[2] dsa - dsa'
        self.assertEqual(expected, mail.show_list(self.lists, 3))

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

    def test_search_email(self):
        mail.add_new_user(self.lists, 1, 'ivan', 'dragan@petkan')
        mail.add_new_user(self.lists, 2, 'ivan', 'dragan@petkan')
        expected = '<dragan@petkan> was found in:\n'\
                '[1] - list1\n[2] - list2'
        self.assertEqual(expected, mail.search_email(self.lists, 'dragan@petkan'))

if __name__ == '__main__':
    unittest.main()

