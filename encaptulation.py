class UserDetails:
    def __init__(self, user_name, password):
        self.user_name = 'alex'
        self.password = 123

    def display_user_name(self):
        return self.user_name

    # This is a private function inside a class which will make it only inheritable
    def _get_password(self):
        return self.password


class AppDetails(UserDetails):
    def show_password(self):
        x = self._get_password()
        print(x)


obj = AppDetails('alex', 123)
obj._get_password()
