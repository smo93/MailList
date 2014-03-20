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

    def test_print_with_something_in_it(self):
        self.maillist.add_user('Ivan', 'vanko98@asd.sd')
        self.maillist.add_user('Peho', 'madafakajones90@gmail.com')

        expected = '[1] Ivan - vanko98@asd.sd\n[2] Peho - madafakajones90@gmail.com'

        self.assertEqual(expected, self.maillist.print_())

    def test_search_email_available(self):
        self.maillist.add_user('Ivan', 'vanko98@asd.sd')
        self.maillist.add_user('Peho', 'madafakajones90@gmail.com')

        check = 'madafakajones90@gmail.com'
        self.assertTrue(self.maillist.search_email(check))


    def test_serach_email_unavailable(self):
        self.maillist.add_user('Ivan', 'vanko98@asd.sd')
        self.maillist.add_user('Peho', 'madafakajones90@gmail.com')

        check = 'plampetrova83@gmail.com'
        self.assertTrue(not self.maillist.search_email(check))

    def test_name_available(self):
        self.maillist.add_user('Ivan', 'vanko98@asd.sd')
        self.maillist.add_user('Peho', 'madafakajones90@gmail.com')

        check = 'Peho'
        self.assertTrue(self.maillist.search_name(check))

    def test_name_unavailable(self):
        self.maillist.add_user('Ivan', 'vanko98@asd.sd')
        self.maillist.add_user('Peho', 'madafakajones90@gmail.com')

        check = 'Georgi'
        self.assertFalse(self.maillist.search_name(check))


if __name__ == '__main__':
    unittest.main()
