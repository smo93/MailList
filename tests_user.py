import user
import unittest

class UserTest(unittest.TestCase):
    """docstring for UserTest"""

    def setUp(self):
        self.user = user.User("Georgi Peev","georgimpeev@gmail.com")


    def tests_init_user(self):
        self.assertTrue(self.user.name is not None)
        self.assertTrue(self.user.email is not None)

    def tests_take_name(self):
        expected = "Georgi Peev"

        self.assertEqual(expected, self.user.take_name())

    def tests_take_email(self):
        expected = "georgimpeev@gmail.com"

        self.assertEqual(expected, self.user.take_email())

if __name__ == '__main__':
    unittest.main()
