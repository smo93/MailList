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

    def tests_update_user_name_changed(self):
        self.user.update_user("Plamena Petrova", "plampetrova83@gmail.com")
        expected1 = "Plamena Petrova"
        expected2 = "plampetrova83@gmail.com"

        self.assertEqual(expected1, self.user.take_name())
        self.assertEqual(expected2, self.user.take_email())

    def tests_update_user_name_untouched(self):
        self.user.update_user("", "madafakajones@gmail.com")
        expected1 = "Georgi Peev"
        expected2 = "madafakajones@gmail.com"

        self.assertEqual(expected1, self.user.take_name())
        self.assertEqual(expected2, self.user.take_email())


if __name__ == '__main__':
    unittest.main()
