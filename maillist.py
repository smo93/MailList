from user import User


class MailList():
    """docstring for MailList"""
    def __init__(self, name):
        self.name = name
        self.users = []

    def get_name(self):
        return self.name

    def add_user(self, user_name, user_email):
        new_user = User(user_name, user_email)
        self.users.append(new_user)

    def print_(self):
        result = []
        index = 1
        for item in self.users:
            result.append(("[%d] %s - %s") % (index, item.name, item.email))
            index += 1
        return '\n'.join(result)

    def search_email(self, email):
        for item in self.users:
            if email == item.email:
                return True
        return False
