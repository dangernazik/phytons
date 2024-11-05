class BankAccount:
    def __init__(self, account_id=None, owner_name=None, balance=0.0):
        self.__account_id = account_id
        self.__owner_name = owner_name
        self.__balance = balance

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = value

    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, value):
        self.__owner_name = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Баланс не може бути меншим за нуль.")
        else:
            self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            print("Сума поповнення повинна бути більше нуля.")
            return
        self.__balance += amount
        print(f"Баланс поповнено на {amount}. Новий баланс: {self.__balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття повинна бути більше нуля.")
            return
        if amount > self.__balance:
            print("Недостатньо коштів на рахунку.")
            return
        self.__balance -= amount
        print(f"Знято {amount}. Новий баланс: {self.__balance}.")

    def __str__(self):
        return f"User ID: {self.__account_id}, Owner: {self.__owner_name}, Balance: {self.__balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_id not in self.accounts:
            self.accounts[account.account_id] = account
            print(f"Акаунт {account.account_id} додано.")
        else:
            print("Акаунт з таким ID вже створено.")

    def remove_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            print(f"Акаунт {account_id} видалено.")
        else:
            print("Акаунт не знайдено.")

    def sort_accounts_by_balance(self):
        return sorted(self.accounts.values(), key=lambda acc: acc.balance, reverse=True)

account1 = BankAccount(1, "Олександр", 1000.0)
account2 = BankAccount(2, "Марія", 500.0)
account3 = BankAccount(3, "Іван", 1500.0)
account4 = BankAccount(4, "Петро", 0.0)

account4.deposit(3000)
account2.withdraw(150)

bank = Bank()
bank.add_account(account1)
bank.add_account(account2)
bank.add_account(account3)
bank.add_account(account4)

sorted_accounts = bank.sort_accounts_by_balance()
print("\nSorted account by balance:")
for account in sorted_accounts:
    print(account)

