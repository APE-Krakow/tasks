class Account:
    def __init__(self, username, password, amount=0):
        self.username = username
        self.password = password
        self.account = amount

    def check_password(self, password: str):
        if password == self.password:
            return true
        else:
            return false

    def transaction(self, amount: int):
        if amount < 0 and amount > self.account:
            raise ValueError("Cannot overdraw account")
        else:
            self.account += amount

    def __list__(self):
        return [self. username, self.password, self.account]

