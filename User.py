class User:
    def __init__(self, id, login, password, role):
        self.id = id
        self.login = login
        self.password = password
        self.role = role

    def __str__(self):
        return f"User(login='{self.login}')"

