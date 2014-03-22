import unittest
import mail
import os
from maillist import MailList
from maillist_factory import MailListFactory
from subprocess import call



class MailTest(unittest.TestCase):
    """docstring for MailTest"""
    def setUp(self):
        self.factory = MailListFactory()
        self.lists = [self.factory.create('list1'), self.factory.create('list2')]

    def test_merge_empty_lists(self):
        mail.merge(self.lists, self.factory, 1, 2, 'list3')
        expected = '[1] - list1\n[2] - list2\n[3] - list3\n'
        self.assertEqual(expected, mail.show_lists(self.lists))

    def test_merge_non_empty_lists(self):
        mail.add_new_user(self.lists, 1, 'asd', 'asd')
        mail.add_new_user(self.lists, 2, 'dsa', 'dsa')
        mail.merge(self.lists, self.factory, 1, 2, 'list3')
        expected = '[1] asd - asd\n[2] dsa - dsa'
        self.assertEqual(expected, mail.show_list(self.lists, 3))

    def test_show_lists(self):
        expected = '[1] - list1\n[2] - list2\n'
        self.assertEqual(expected, mail.show_lists(self.lists))

    def test_show_list(self):
        self.lists[0].add_user('ivan', 'dragan@petkan')
        self.assertEqual('[1] ivan - dragan@petkan', mail.show_list(self.lists, 1))

    def test_show_list_with_bad_id(self):
        self.assertFalse(mail.show_list(self.lists, 3))

    def test_create_list(self):
        lists = []
        m = MailListFactory()
        mail.create_list(lists, m, 'list1')
        self.assertEqual('[1] - list1\n', mail.show_lists(lists))

    def test_add_new_user(self):
        result = mail.add_new_user(self.lists, 1, 'ivan', 'dragan@petkan')
        self.assertTrue(result)
        print(mail.show_list(self.lists, 1))
        self.assertEqual('[1] ivan - dragan@petkan', mail.show_list(self.lists, 1))

    def test_add_new_user_in_non_existent_list(self):
        self.assertFalse(mail.add_new_user(self.lists, 4, 'a', 'b'))

    def test_search_email(self):
        mail.add_new_user(self.lists, 1, 'ivan', 'dragan@petkan')
        mail.add_new_user(self.lists, 2, 'ivan', 'dragan@petkan')
        expected = '<dragan@petkan> was found in:\n'\
                '[1] - list1\n[2] - list2'
        self.assertEqual(expected, mail.search_email(self.lists,
            'dragan@petkan'))

    def test_export_list_to_json(self):
        mail.export(self.lists, 1)
        expected = ['{"_MailList__id": 1, "_MailList__name": "list1", "users": []}',
                    '{"_MailList__id": 1, "users": [], "_MailList__name": "list1"}',
                    '{"_MailList__name": "list1", "_MailList__id": 1, "users": []}',
                    '{"_MailList__name": "list1", "users": [], "_MailList__id": 1}',
                    '{"users": [], "_MailList__name": "list1", "_MailList__id": 1}',
                    '{"users": [], "_MailList__id": 1, "_MailList__name": "list1"}']
        exp_file = open('list1.json', 'r')
        actual = exp_file.read()
        exp_file.close()
        self.assertIn(actual, expected)
        call('rm list1.json', shell=True)

    def test_import_list_from_json(self):
        call('echo \'{\"name\": \"list3\", \"users\":'\
                '[{\"name\": \"asd\", \"email\": \"asd\"}]}\' > list3.json',
                shell=True)
        mail.import_json(self.lists, self.factory, 'list3.json')
        self.assertEqual('list3', self.lists[2].get_name())
        call('rm list3.json', shell=True)

    def test_remove_subscriber(self):
        self.lists[0].add_user('ivan', 'dragan@petkan')
        self.lists[0].add_user('georgi', 'georgipeev@gmail.com')
        mail.remove_subscriber(self.lists, 1, 2)
        self.assertEqual('[1] ivan - dragan@petkan', mail.show_list(self.lists, 1))





if __name__ == '__main__':
    unittest.main()

