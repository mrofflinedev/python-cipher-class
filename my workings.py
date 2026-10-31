# ATM simulation
# Start with Ksh 1000 balance and offer menu choices.

balance = 1000.0


def run_atm():
    global balance

    while True:
        print("\nATM Menu")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        option = input("Choose an option: ").strip().lower()

        if option in ["1", "check balance", "check"]:
            print(f"Your balance is Ksh {balance:.2f}")

        elif option in ["2", "deposit"]:
            try:
                deposit = float(input("Enter the amount to deposit: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if deposit > 0:
                balance += deposit
                print(f"Deposit successful. New balance: Ksh {balance:.2f}")
            else:
                print("Deposit amount must be greater than zero.")

        elif option in ["3", "withdraw", "withdraw funds"]:
            try:
                withdraw = float(input("Enter the amount to withdraw: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if withdraw > 0:
                if balance >= withdraw:
                    balance -= withdraw
                    print(f"Withdrawal successful. Remaining balance: Ksh {balance:.2f}")
                else:
                    print("Inadequate funds in your account")
            else:
                print("Withdrawal amount must be greater than zero.")

        elif option in ["4", "exit"]:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid option. Please try again.")


# Movie ticket pricing based on age, day, and student status.

def get_movie_ticket_price():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                break
            print("Age cannot be negative.")
        except ValueError:
            print("Please enter a valid whole number for your age.")

    while True:
        day = input("Is it a weekday or weekend? ").strip().lower()
        if day in ["weekday", "weekend"]:
            break
        print("Please enter 'weekday' or 'weekend'.")

    while True:
        student = input("Are you a student with a valid ID? (yes/no): ").strip().lower()
        if student in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'.")

    if student == "yes":
        ticket_price = 10
    elif age < 12:
        ticket_price = 8 if day == "weekday" else 10
    elif age >= 65:
        ticket_price = 9 if day == "weekday" else 11
    else:
        ticket_price = 12 if day == "weekday" else 15

    print(f"Your movie ticket costs ${ticket_price}.")


# Abstract class and patient model demonstrating OOP.

from abc import ABC, abstractmethod


class HospitalService(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class Patient(HospitalService):
    def __init__(self, name, patient_id, phone, age, account_balance):
        self.name = name
        self.patient_id = patient_id
        self.phone = phone
        self.age = age
        self.__balance = account_balance

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient amount")
        return self.__balance

    def display_details(self):
        print("Patient details")
        print(f"Patient name: {self.name}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Phone number: {self.phone}")
        print(f"Age: {self.age}")
        print(f"Account balance: Ksh {self.__balance:.2f}")

    def process_payment(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Payment successful!")
            return True
        print("Payment not successful!")
        return False


class Doctor:
    def __init__(self, doctor_name, doctor_id, specialization, consultation_fee):
        self.name = doctor_name
        self.id = doctor_id
        self.specialization = specialization
        self.fee = consultation_fee

    def display_details(self):
        print("Doctor details")
        print(f"Doctor's name: {self.name}")
        print(f"Doctor's ID: {self.id}")
        print(f"Specialization: {self.specialization}")
        print(f"Consultation fee: {self.fee}")


class Outpatient(Patient):
    def patient_type(self):
        print("Outpatient Patient")

    def payment(self, amount, consultation_fee):
        total = consultation_fee + 100
        if amount >= total:
            print("Payment successful!")
            return total
        print("Insufficient amount payment not successful!")
        return 0


class Inpatient(Patient):
    def patient_type(self):
        print("Inpatient patient")

    def payment(self, amount, consultation_fee):
        total = consultation_fee + 200
        if amount >= total:
            print("Payment successful!")
            return total
        print("Insufficient amount payment not successful!")
        return 0


class Appointment:
    def __init__(self, doctor_object, patient_object, appointment_date, appointment_time):
        self.doctor = doctor_object
        self.patient = patient_object
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.status = "confirmed"
        
    def display_details(self):
        print("Appointment details")
        print(f"Doctor: {self.doctor.name}")
        print(f"Patient: {self.patient.name}")
        print(f"Appointment Date: {self.appointment_date}")
        print(f"Appointment Time: {self.appointment_time}")
        print(f"Appointment Status: {self.status}")

# Method to confirm an appointment
def __init__(self,confirmed,cancelled):
  if self.status=="confirmed":
    print("Appointment successfully confirmed!")
  else:
      print("Appointment cancelled")
      
# method for cancelling appointment
def __init__(self,confirmed,cancelled):
    if self.status=="cancelled":
        print("Appointment cancelled!")
    else:
        print("")          
    
    