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
