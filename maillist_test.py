import unittest
from maillist import MailList
from user import User


class MailListTest(unittest.TestCase):
    """docstring for MailListTest"""
    def setUp(self):
        self.maillist = MailList('new list')

    def test_get_name(self):
        self.assertEqual('new list', self.maillist.get_name())

    def test_add_user(self):
        self.maillist.add_user('Ivan', 'vanko98@asd.sd')
        expected_user = User('Ivan', 'vanko98@asd.sd')
        self.assertEqual(expected_user.take_name(), self.maillist.users[0].take_name())
        self.assertEqual(expected_user.take_email(), self.maillist.users[0].take_email())

if __name__ == '__main__':
    unittest.main()
