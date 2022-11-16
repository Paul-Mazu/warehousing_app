class User:

    def __init__(self, user_name=None) -> None:
        pass
    
    def set_username(self):
        while True:
            user_name = input("What is your user name?: ")
            if len(user_name):
                self.user_name = user_name
                break
            else:
                print('Please input your user name')