from sample.data import personnel


class User:

    def __init__(self, user_name='Guest', password=None) -> None:
        self.user_name = user_name
        self.password = password
        if user_name == 'Guest':
            self.allowed = False
        else:
            self.allowed = True
        self.history = []

    def print_history(self):
        for el in self.history:
            print(el)
