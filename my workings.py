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
        print(f"Account balance: Ksh {self.__balance}")

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
        return "Outpatient Patient"

    def payment(self, amount, consultation_fee):
        total = consultation_fee + 100
        if amount >= total:
            print("Payment successful!")
            return total
        print("Insufficient amount payment not successful!")
        return 0


class Inpatient(Patient):
    def patient_type(self):
        return "Inpatient patient"

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

    def confirm(self):
        if self.status == "cancelled":
            print("A cancelled appointment cannot be confirmed.")
            return
        self.status = "confirmed"
        print("Appointment successfully confirmed!")

    def cancel(self):
        if self.status == "cancelled":
            print("Appointment is already cancelled.")
            return
        self.status = "cancelled"
        print("Appointment cancelled!")


patients_list = []
doctors_list = []
appointments_list = []


def _read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def _read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def register_patient():
    patient_id = _read_int("Enter Patient ID: ")
    if any(patient.patient_id == patient_id for patient in patients_list):
        print("A patient with that ID is already registered.")
        return

    name = input("Enter Patient Name: ").strip()
    age = _read_int("Enter Patient Age: ")
    while age < 0:
        print("Age cannot be negative.")
        age = _read_int("Enter Patient Age: ")
    phone = input("Enter Patient Phone Number: ").strip()

    new_patient = Patient(name, patient_id, phone, age, 0.0)
    patients_list.append(new_patient)
    print(f"Patient {name} registered successfully!")
    return new_patient


def register_doctor():
    doctor_id = _read_int("Enter Doctor ID: ")
    if any(doctor.id == doctor_id for doctor in doctors_list):
        print("A doctor with that ID is already registered.")
        return

    name = input("Enter Doctor Name: ").strip()
    specialization = input("Enter Doctor Specialization: ").strip()
    consultation_fee = _read_float("Enter Consultation Fee: ")
    while consultation_fee < 0:
        print("Consultation fee cannot be negative.")
        consultation_fee = _read_float("Enter Consultation Fee: ")

    new_doctor = Doctor(name, doctor_id, specialization, consultation_fee)
    doctors_list.append(new_doctor)
    print(f"Doctor {name} registered successfully!")
    return new_doctor


def display_all_patients():
    print("All Registered Patients")
    if not patients_list:
        print("No patients registered.")
        return
    for patient in patients_list:
        print(
            f"Patient ID: {patient.patient_id}, Name: {patient.name}, "
            f"Age: {patient.age}, Phone: {patient.phone}"
        )


def display_all_doctors():
    print("All Registered Doctors")
    if not doctors_list:
        print("No doctors registered.")
        return
    for doctor in doctors_list:
        print(
            f"Doctor ID: {doctor.id}, Name: {doctor.name}, "
            f"Specialization: {doctor.specialization}, "
            f"Consultation Fee: Ksh {doctor.fee:.2f}"
        )


def display_appointments():
    print("All Appointments")
    if not appointments_list:
        print("No appointments scheduled.")
        return
    for appointment in appointments_list:
        appointment.display_details()


def search_patient():
    patient_id = _read_int("Enter Patient ID to search: ")
    patient = next(
        (patient for patient in patients_list if patient.patient_id == patient_id),
        None,
    )
    if patient is None:
        print("Patient not found.")
        return None
    print(
        f"Patient ID: {patient.patient_id}, Name: {patient.name}, "
        f"Age: {patient.age}, Phone: {patient.phone}"
    )
    return patient


def search_doctor():
    doctor_id = _read_int("Enter Doctor ID to search: ")
    doctor = next((doctor for doctor in doctors_list if doctor.id == doctor_id), None)
    if doctor is None:
        print("Doctor not found.")
        return None
    print(
        f"Doctor ID: {doctor.id}, Name: {doctor.name}, "
        f"Specialization: {doctor.specialization}"
    )
    return doctor


def search_appointments_by_date():
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
    matches = [
        appointment
        for appointment in appointments_list
        if appointment.appointment_date == appointment_date
    ]
    if not matches:
        print(f"No appointments found on {appointment_date}.")
        return []
    for appointment in matches:
        appointment.display_details()
    return matches


def book_appointment():
    doctor_id = _read_int("Enter Doctor ID for the appointment: ")
    patient_id = _read_int("Enter Patient ID for the appointment: ")
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
    appointment_time = input("Enter Appointment Time (HH:MM): ").strip()

    doctor = next((doctor for doctor in doctors_list if doctor.id == doctor_id), None)
    patient = next(
        (patient for patient in patients_list if patient.patient_id == patient_id),
        None,
    )
    if doctor is None or patient is None:
        print("Invalid Doctor ID or Patient ID. Please register them first.")
        return None

    appointment = Appointment(doctor, patient, appointment_date, appointment_time)
    appointments_list.append(appointment)
    print(
        f"Appointment booked successfully for {patient.name} with "
        f"Dr. {doctor.name} on {appointment_date} at {appointment_time}."
    )
    return appointment


def run_hospital_system():
    while True:
        print("\nHospital Management Menu")
        print("1. Register a patient")
        print("2. Register a doctor")
        print("3. Display patients")
        print("4. Display doctors")
        print("5. Book an appointment")
        print("6. Display appointments")
        print("7. Search for a patient")
        print("8. Search for a doctor")
        print("9. Search appointments by date")
        print("10. Exit")

        option = input("Choose an option: ").strip()
        actions = {
            "1": register_patient,
            "2": register_doctor,
            "3": display_all_patients,
            "4": display_all_doctors,
            "5": book_appointment,
            "6": display_appointments,
            "7": search_patient,
            "8": search_doctor,
            "9": search_appointments_by_date,
        }
        if option == "10":
            print("Exiting the hospital management system.")
            return
        action = actions.get(option)
        if action is None:
            print("Invalid option. Please try again.")
        else:
            action()


if __name__ == "__main__":
    run_hospital_system()
