import json
import pandas as pd
from bank_user import Account


class AccountManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.accounts = self.load_users(filename)

    def load_users(self, filename):
        result = {}
        try:
            file = open(filename, "rt")
        except FileNotFoundError:
            return result
        try:
            previous_data = json.load(file)
        except json.JSONDecodeError:
            return result
        file.close()
        users = [Account(*data) for data in previous_data]
        for user_id, user in enumerate(users):
            result[user_id] = user
        return result

    def user_exists(self, username):
        if [user for user in self.accounts.values() if user.username == username]:
            return True
        else:
            return False

    def add_user(self, username, password):
        if not self.user_exists(username):
            self.accounts[len(self.accounts)] = Account(username, password)
        else:
            raise KeyError

    def get_user_id(self, username):
        for key, user in self.accounts.items():
            if user.username == username:
                return key
        return None

    def check_password(self, user_id, password):
        if self.accounts[user_id].check_password:
            return True
        else:
            return False

    def add_money(self, user_id, amount):
        self.accounts[user_id].transaction(amount)

    def transfer_money(self, user_id, recipient_name, amount):
        recipient_id = self.get_user_id(recipient_name)
        if recipient_id == None:
            raise KeyError
        elif int(amount) < 0:
            raise ValueError("Przelew nie może być ujemny")
        elif int(amount) > self.accounts[user_id].account:
            raise ValueError("brak odpowiednich środków")
        else:
            self.accounts[user_id].transaction(-1*int(amount))
            self.accounts[recipient_id].transaction(int(amount))

    def print_state(self, user_id):
        print(str(self.accounts[user_id].account))

    def save_data(self):
        with open(self.filename, "wt") as file:
            result = [account.__list__() for account in self.accounts.values()]
            json.dump(result, file)

    def export(self):
        df = pd.DataFrame()
        df["Nazwa Użytkownika"] = pd.Series([user.username for user in self.accounts.values()])
        df["Stan Konta"] = pd.Series([user.account for user in self.accounts.values()])
        df.to_excel("bank.xlsx")
    
    

    
