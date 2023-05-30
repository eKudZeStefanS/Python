class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Депозит одобрен! Сейчас ваш счет составляет: ", self.__balance)
        else:
            print("Неверная сумма депозита!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Вывод одобрен! Сейчас ваш счет составляет:", self.__balance)
        else:
            print("Неверная сумма для вывода или недостаточно средств!")


account = BankAccount('123', 1000)
print(account.get_account_number())
print(account.get_balance())

account.deposit(500)
account.withdraw(200)
