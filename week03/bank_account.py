class BankAccount:
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.record = ["Account was created"]

    def deposit(self, amount):
        self.balance += amount
        self.record.append("Deposited {}$".format(amount))

    def withdraw(self, amount):
        self.balance -= amount
        self.record.append("{}$ was withdrawed".format(amount))
    
    def balance(self):
        self.record.append("Balance check -> {}$".format(self.balance))
        return self.balance

    def __str__(self):
        #self.record.append("Balance check -> {}$".format(self.balance))
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        self.record.append("__int__ check -> {}$".format(self.balance))
        return int(self.balance)

    def __eq__(self, other):
        return self.currency == other.currency

    def transfer_to(self, account, amount):
        if self.__eq__(account):
            account.balance += amount
            self.balance -= amount
            self.record.append("Transfer to {} for {}{}".format(account.name, amount, account.currency))
            account.record.append("Transfer from {} for {}{}".format(self.name, amount, account.currency))
            return True
        else:
            return False

    def history(self):
        return self.record

account = BankAccount("Rado", 0, "$")
print(account)
account.deposit(1000)
account.balance()
str(account)
int(account)
account.history()
account.withdraw(500)
account.balance()
print(account.history())
account.withdraw(1000)
account.balance()
print(account.history())