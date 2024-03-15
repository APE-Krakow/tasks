from account_manager import AccountManager


class Bank:
    def __init__(self, filename):
        self.account_manager = AccountManager(filename)

    def run(self):
        while(True):
            x = input("Dodaj użytkownika/Zaloguj się/Wyjdź/Eksportuj\n")
            if x == "D":
                username = input("Podaj nazwe uzytkownika\n")
                password = input("Wpisz nowe hasło\n")
                try:
                    self.account_manager.add_user(username, password)
                except KeyError:
                    print("Użytkownik już istnieje")
            elif x == "Z":
                username = input("Podaj login\n")
                password = input("Podaj haslo\n")
                user_id = self.account_manager.get_user_id(username)
                if user_id == None:
                    print("nie ma takiego użytkownika")
                elif not self.account_manager.check_password(user_id, password):
                    print("nieprawidłowe hasło")
                else:
                    self.run_user(user_id)
            elif x == "E":
                self.account_manager.export()
            elif x == "W":
                self.account_manager.save_data()
                break
    
    def run_user(self, user_id):
        while(True):
            x = input("Dodaj pieniądze/Wyświetl stan/Przelej pieniądze/Zamknij\n")
            if x == "D":
                amount = input("Ile chcesz wpłacić?\n")
                self.account_manager.add_money(user_id, int(amount))
            elif x == "P":
                recipient_id = input("Jakiemu użytkownikowi przekazujesz pieniądze?\n")
                amount = input("Jaką ilość przekazujesz?\n")
                try:
                    self.account_manager.transfer_money(user_id, recipient_id, int(amount))
                except KeyError:
                    print("Nie ma takiego użytkownika")
                except ValueError:
                    print("Nie posiadasz wystarczających środków")
            elif x == "W":
                self.account_manager.print_state(user_id)
            elif x == "Z":
                break

if __name__ == "__main__":
    my_bank = Bank("bank_data.json")
    my_bank.run()
