"""
Encapsulation

Encapsulation controls how internal data is accessed or modified.
"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance


account = BankAccount("Bharadwaj", 1000)

print(f"Owner: {account.owner}")
print(f"Balance: {account.get_balance()}")

account.deposit(500)
print(f"Balance: {account.get_balance()}")

account.withdraw(300)
print(f"Balance: {account.get_balance()}")

account.withdraw(2000)
print(f"Balance: {account.get_balance()}")


# AI-oriented example


class APIKeyManager:
    def __init__(self, api_key):
        self.__api_key = api_key

    def is_configured(self):
        return bool(self.__api_key)

    def masked_key(self):
        if not self.__api_key:
            return "No API key configured"

        return f"{self.__api_key[:4]}****"


key_manager = APIKeyManager("abcd123456789")

print(f"API key configured: {key_manager.is_configured()}")
print(f"Masked API key: {key_manager.masked_key()}")
