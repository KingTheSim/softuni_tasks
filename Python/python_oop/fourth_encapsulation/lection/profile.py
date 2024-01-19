class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        length = len(value) >= 8
        upper = bool([c for c in value if c.isupper()])
        number = bool([n for n in value if n.isdigit()])

        if length and upper and number:
            self.__password = value
        else:
            raise ValueError("The password must be 8"
                             " or more characters with at least 1 digit"
                             " and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
