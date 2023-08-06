from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number  # Encapsulation: Private attribute
        self.holder_name = holder_name
        self.__balance = balance  # Encapsulation: Private attribute

    def __str__(self):
        return f"{self.holder_name}'s Account (Account Number: {self.__account_number})"

    @property  # Abstraction: Property getter for balance attribute
    def balance(self):
        return self.__balance

    @abstractmethod  # Abstraction: Abstract method
    def deposit(self, amount):
        pass

    @abstractmethod  # Abstraction: Abstract method
    def withdraw(self, amount):
        pass


class CheckingAccount(Account):  # Inheritance
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.__overdraft_limit = overdraft_limit  # Encapsulation: Private attribute

    @property  # Abstraction: Property getter for overdraft_limit attribute
    def overdraft_limit(self):
        return self.__overdraft_limit

    @overdraft_limit.setter  # Abstraction: Property setter for overdraft_limit attribute
    def overdraft_limit(self, new_limit):
        self.__overdraft_limit = new_limit

    def deposit(self, amount):  # Polymorphism
        self.__balance += amount

    def withdraw(self, amount):  # Polymorphism
        if self.__balance - amount >= -self.__overdraft_limit:  # Encapsulation: Accessing private attribute
            self.__balance -= amount
            return True
        else:
            return False


class SavingsAccount(Account):  # Inheritance
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.__interest_rate = interest_rate  # Encapsulation: Private attribute

    @property  # Abstraction: Property getter for interest_rate attribute
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter  # Abstraction: Property setter for interest_rate attribute
    def interest_rate(self, new_rate):
        self.__interest_rate = new_rate

    def deposit(self, amount):  # Polymorphism
        self.__balance += amount

    def withdraw(self, amount):  # Polymorphism
        if self.__balance - amount >= 0:  # Encapsulation: Accessing private attribute
            self.__balance -= amount
            return True
        else:
            return False


# Example usage: (Unchanged)
checking_account = CheckingAccount("12345", "John Doe", 1000, overdraft_limit=500)
savings_account = SavingsAccount("67890", "Alice Smith", 5000, interest_rate=0.02)

print(checking_account)
print(savings_account)

# Use the property getters and setters
checking_account.deposit(500)
print(f"Checking Account Balance: {checking_account.balance} USD")  # Encapsulation: Using property getter

savings_account.withdraw(3000)
print(f"Savings Account Balance: {savings_account.balance} USD")  # Encapsulation: Using property getter

# Use the property setters
checking_account.overdraft_limit = 600  # Encapsulation: Using property setter
print(f"New Overdraft Limit: {checking_account.overdraft_limit} USD")  # Encapsulation: Using property getter

savings_account.interest_rate = 0.025  # Encapsulation: Using property setter
print(f"New Interest Rate: {savings_account.interest_rate * 100}%")  # Encapsulation: Using property getter


# Encapsulation: The Account, CheckingAccount, and SavingsAccount classes have private attributes 
# like __account_number, __balance, __overdraft_limit, and __interest_rate. We encapsulate these attributes to protect them 
# from direct access outside their respective classes. We also use the property getters and setters to control access to these private attributes.

# Abstraction: The Account class is an abstract class due to the presence of abstract methods deposit and withdraw. 
# It defines a common interface for all types of accounts, hiding the implementation details in its subclasses. 
# Additionally, the property getters and setters provide an abstract interface to access and modify the private attributes.

# Inheritance: The CheckingAccount and SavingsAccount classes inherit from the Account class, inheriting its attributes and methods.

# Polymorphism: Both CheckingAccount and SavingsAccount classes override the deposit and withdraw methods to provide specific 
# behavior for each type of account. This demonstrates polymorphism by allowing different account types to have their own 
# implementation of the same methods with different behaviors.