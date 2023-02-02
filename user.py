from cli.data import personnel


class User:
    def __init__(self, user_name='Guest', password=None) -> None:
        self.user_name = user_name
        self.password = password
        if self.user_validation(personnel):
            self.validated = True
        else:
            self.validated = False
        self.history = []

    def user_validation(self, lst):
        for dic in lst:
            if dic.get('user_name') == self.user_name and dic.get('password') == self.password:
                return True
            elif dic.get('head_of') is not None:
                if self.user_validation(dic['head_of']):
                    return True
        return False

    def add_to_history(self, action):
        self.history.append(action)

    def print_history(self):
        for el in self.history:
            print(el)

    def greet(self):
        return f'''Hello, {self.user_name}!
                Welcome to our Warehouse Database.
                If you don't find what you are looking for,
                please ask one of our staff members to assist you.
                '''
