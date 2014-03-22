from maillist_factory import MailListFactory
import unittest


class MailListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = MailListFactory()

    def test_next_id(self):
        self.assertEqual(1, self.factory.get_next_id())

    def test_create(self):
        m = self.factory.create('asd')
        self.assertEqual('asd', m.get_name())

if __name__ == '__main__':
    unittest.main()
