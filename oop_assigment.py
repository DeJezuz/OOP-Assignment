# Base class: BankAccount
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # Encapsulation: Getters
    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited €{amount}. New balance: €{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew €{amount}. New balance: €{self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # Display balance
    def display_balance(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: €{self.__balance}")

# Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = interest_rate

    # Polymorphism: Overriding display_balance
    def display_balance(self):
        interest = self.get_balance() * self.__interest_rate
        total = self.get_balance() + interest
        print(f"Account Holder: {self.get_account_holder()}")
        print(f"Balance: €{self.get_balance()} + Interest: €{interest:.2f} = Total: €{total:.2f}")

    # Method to apply interest
    def apply_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Interest of €{interest:.2f} applied.")

# Example usage
if __name__ == "__main__":
    # Create a regular account
    acc1 = BankAccount("FR123", "Gervásio", 500)
    acc1.deposit(200)
    acc1.withdraw(100)
    acc1.display_balance()

    print("\n---\n")

    # Create a savings account
    acc2 = SavingsAccount("FR456", "Gervásio", 1000)
    acc2.display_balance()
    acc2.apply_interest()
    acc2.display_balance()
