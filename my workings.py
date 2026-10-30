# create a program that simulates a bank ATM
# start with ksh1000 present account balance
# present a menu with options: check balance, deposit, withdraw and exit

balance = 1000.0

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
        deposit = float(input("Enter the amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f"Deposit successful. New balance: Ksh {balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    elif option in ["3", "withdraw", "withdraw funds"]:
        withdraw = float(input("Enter the amount to withdraw: "))
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

# write a program that calculates the cost of movie tickets based on customer details
# ask the user for their age, weekday or weekend, student or not
# children (under 12): $8 on weekdays and $10 on weekends
# senior (65+): $9 on weekdays and $11 on weekends
# students: flat $10 rate with ID
# regular adults: $12 on weekdays and $15 on weekends

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
