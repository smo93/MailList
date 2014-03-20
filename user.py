class User():
    """docstring for User"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def take_name(self):
        return self.name

    def take_email(self):
        return self.email

    def update_user(self, name, email):
        if name == '':
            pass
        else:
            self.name = name
        self.email = email


