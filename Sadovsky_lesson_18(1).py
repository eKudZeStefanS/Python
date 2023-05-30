class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Неверная сумма депозита!")
            self.__balance += amount
            print("Депозит одобрен! Сейчас ваш счет составляет: ", self.__balance)
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0 or amount > self.__balance:
                raise ValueError("Неверная сумма для вывода или недостаточно средств!")
            self.__balance -= amount
            print("Вывод одобрен! Сейчас ваш счет составляет:", self.__balance)
        except ValueError as e:
            print(e)


account = BankAccount('123', 1000)
print(account.get_account_number())
print(account.get_balance())

account.deposit('500')
account.withdraw('200.5')

account.deposit('0')
account.withdraw('2000')

account.deposit('-10')
account.withdraw('-500')