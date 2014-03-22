from user import User


class MailList():
    """docstring for MailList"""
    def __init__(self, list_id, name):
        self.__id = list_id
        self.__name = name
        self.users = []

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def add_user(self, user_name, user_email):
        new_user = User(user_name, user_email)
        self.users.append(new_user)

    def print_(self):
        result = []
        index = 1
        for item in self.users:
            result.append('[{0}] {1} - {2}'.format(index, item.name, item.email))
            index += 1
        return '\n'.join(result)

    def search_email(self, email):
        for item in self.users:
            if email == item.email:
                return True
        return False

    def search_name(self, name):
        for item in self.users:
            if name == item.name:
                return True
        return False

