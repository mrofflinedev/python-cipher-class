class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# object
student1 = Student("Collins", 21)
print(student1.name)
print(f"Student name: {student1.name}")
print(f"Age: {student1.age}")


from abc import ABC, abstractmethod

# ==================================
# 1. ABSTRACTION
# ==================================

# Abstract class defining a common payment structure
class MpesaPayment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


# ==================================
# 2. CLASS AND ENCAPSULATION
# ==================================

class MpesaAccount(MpesaPayment):

    # Constructor: initializes customer details
    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone

        # Private-like attribute to protect balance
        self.__balance = balance

    # Method for checking account balance
    def check_balance(self):
        return self.__balance

    # Method for depositing money
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")

        else:
            print("Invalid deposit amount!")

    # Method for withdrawing money
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount!")

        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")

        else:
            print("Insufficient balance!")

    # Method for sending money to another customer
    def send_money(self, receiver, amount):

        if amount <= 0:
            print("Invalid amount!")

        elif amount > self.__balance:
            print("Insufficient balance!")

        else:
            self.__balance -= amount
            receiver.deposit(amount)

            print(f"Ksh {amount} sent to {receiver.name}")

    # Implementing the abstract payment method
    def make_payment(self, amount):
        self.withdraw(amount)


# ==================================
# 3. INHERITANCE
# ==================================

# CustomerAccount inherits from MpesaAccount
class CustomerAccount(MpesaAccount):

    def account_type(self):
        print("Personal M-PESA Account")


# BusinessAccount also inherits from MpesaAccount
class BusinessAccount(MpesaAccount):

    def account_type(self):
        print("Business M-PESA Account")


# ==================================
# 4. CREATING OBJECTS
# ==================================

# Creating three customer objects
eric = CustomerAccount("Eric", "0712345678", 5000)

john = CustomerAccount("John", "0723456789", 3000)

shop = BusinessAccount("Eric Shop", "0734567890", 10000)


# ==================================
# 5. POLYMORPHISM 
# ==================================

# Different objects have the same method name
# but produce different behaviours

eric.account_type()
shop.account_type()


# ==================================
# 6. INTERACTING WITH THE SYSTEM
# ==================================

# Display customer information
print("\n--- M-PESA SYSTEM ---")

print("Customer:", eric.name)
print("Phone:", eric.phone)
print("Balance:", eric.check_balance())


# Deposit money
print("\n--- DEPOSIT ---")
eric.deposit(2000)


# Withdraw money
print("\n--- WITHDRAW ---")
eric.withdraw(1000)


# Send money to another customer
print("\n--- SEND MONEY ---")
eric.send_money(john, 1500)


# Make a payment using abstraction
print("\n--- PAYMENT ---")
eric.make_payment(500)


# Display final balances
print("\n--- FINAL BALANCES ---")

print("Eric:", eric.check_balance())
print("John:", john.check_balance())
print("Shop:", shop.check_balance())