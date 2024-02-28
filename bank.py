import json
import pandas as pd

class Bank:
    def __init__(self, filename: str):
        self.filename = filename
        self.accounts = {}
        self.logged_user = None
        try:
            with open(filename, "rt") as file:
                self.accounts = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def add_user(self, username):
        if username not in self.accounts:
            self.accounts[username] = 0
        else:
            raise KeyError

    def add_money(self, amount):
        self.accounts[self.logged_user] += amount

    def transfer_money(self, user, amount):
        if user not in self.accounts:
            raise KeyError
        elif int(amount) > self.accounts[self.logged_user]:
            raise ValueError
        else:
            self.accounts[self.logged_user] -= int(amount)
            self.accounts[user] += int(amount)

    def print_state(self):
        print(str(self.accounts[self.logged_user]))

    def save_data(self):
        with open(self.filename, "wt") as file:
            json.dump(self.accounts, file)

    def export(self):
        df = pd.DataFrame()
        df["Nazwa Użytkownika"] = pd.Series([key for key in self.accounts.keys()])
        df["Stan Konta"] = pd.Series([value for value in self.accounts.values()])
        df.to_excel("bank.xlsx")
    
    def run_user(self, username):
        if username not in self.accounts:
            raise KeyError
        else:
            self.logged_user = username
        while(True):
            x = input("Dodaj pieniądze/Wyświetl stan/Przelej pieniądze/Zamknij\n")
            if x == "D":
                amount = input("Ile chcesz wpłacić?\n")
                self.add_money(int(amount))
            elif x == "P":
                user = input("Jakiemu użytkownikowi przekazujesz pieniądze?\n")
                amount = input("Jaką ilość przekazujesz?\n")
                try:
                    self.transfer_money(user, int(amount))
                except KeyError:
                    print("Nie ma takiego użytkownika")
                except ValueError:
                    print("Nie posiadasz wystarczających środków")
            elif x == "W":
                self.print_state()
            elif x == "Z":
                break

    def run(self):
        while(True):
            x = input("Dodaj użytkownika/Zaloguj się/Wyjdź/Eksportuj\n")
            if x == "D":
                name = input("Podaj nazwe uzytkownika\n")
                try:
                    self.add_user(name)
                except KeyError:
                    print("Użytkownik już istnieje")
            elif x == "Z":
                name = input("Podaj login\n")
                try:
                    self.run_user(name)
                except KeyError:
                    print("nie ma takiego użytkownika")
            elif x == "E":
                self.export()
            elif x == "W":
                self.save_data()
                break

if __name__ == "__main__":
    my_bank = Bank("bank_data.json")
    my_bank.run()
