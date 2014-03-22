from maillist import MailList


class MailListFactory():
    """docstring for MailListFactory"""
    def __init__(self):
        self.__current_id = 1

    def get_next_id(self):
        res = self.__current_id
        self.__current_id += 1

        return res

    def create(self, name):
        m = MailList(self.get_next_id(), name)
        return m
