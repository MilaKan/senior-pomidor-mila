class BankAccount:
    def __init__(self, owner,balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount
        print(f"Баланс пополнен на сумму: {amount}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        print(f"С вашего счёта списано: {amount}")
    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, owner ,balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        if self.get_balance() > 0:
            interest = self.get_balance() * self.interest_rate
            self.deposit(interest)
            print(f"Начислено процентов: {self.interest_rate} на остаток по счёту")

class CheckingAccount(BankAccount):
    def __init__(self, owner ,balance=0):
        super().__init__(owner , balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        self._BankAccount__balance -= amount
        print(f"С вашего счёта списано: {amount} (овердрафт разрешен)")

if __name__ == "__main__":
    regular_account = BankAccount("Мила", 0)
    regular_account.deposit(500)
    regular_account.withdraw(100)
    savings = SavingsAccount("Милана", 400)
    savings.withdraw(100)
    savings.apply_interest()
    assert savings.get_balance() > 0 , "Баланс должен быть положительным"
    print(f"Сберегательный счет: {savings.get_balance()}")
    checking = CheckingAccount("Милана", 300)
    checking.withdraw(100)
    print(f"Расчетный счет: {checking.get_balance():.2f}")